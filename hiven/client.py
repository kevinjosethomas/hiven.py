import inspect
import aiohttp
import asyncio
import logging
from typing import Coroutine, List

from hiven.core import Command, Context
from hiven.util import format_exception
from hiven.gateway import HTTPClient, WebSocketClient
from hiven.errors import EventHandlerError, CommandAlreadyExists, MissingRequiredArgument

AVAILABLE_EVENTS = ("ready", "message")


class Client:
    def __init__(self, prefix: str, bot: bool = True, case_sensitive: bool = False):
        self.bot = bot
        self.prefix = prefix
        self.case_sensitive = case_sensitive

        self._loop = asyncio.get_event_loop()
        self._logger = logging.getLogger("hiven")

        self.is_ready = False
        self._expected_houses_len = None

        self.event_handlers = {}
        self.command_handlers = {}

        self.user = None
        self.houses = {}

    def event(self, awaitable: Coroutine):
        """Decorator to recognize a function as an event handler"""

        if not inspect.iscoroutinefunction(awaitable):
            return TypeError(f"Expected a coroutine function, received {type(awaitable)}")

        event_name = awaitable.__name__.replace("on_", "")
        if event_name not in AVAILABLE_EVENTS:
            raise EventHandlerError(f"Invalid event handler name, received {event_name}")

        if self.event_handlers.get(event_name):
            self.event_handlers[event_name].append(awaitable)
        else:
            self.event_handlers[event_name] = [awaitable]

        return awaitable

    def command(
        self, awaitable: Coroutine, name: str = None, description: str = None, usage: str = None, aliases: List[str] = None
    ):
        """Decorator to recognize a function as a command"""

        if not inspect.iscoroutinefunction(awaitable):
            return TypeError(f"Expected a coroutine function, received {type(awaitable)}")

        name = name if name else awaitable.__name__

        if self.command_handlers.get(name):
            raise CommandAlreadyExists(f"Command with name {name} already exists!")
        if aliases:
            for alias in aliases:
                if self.command_handlers.get(alias):
                    raise CommandAlreadyExists(f"Command with alias {alias} already exists!")

        description = description if description else awaitable.__doc__
        usage = usage if usage else f"{self.prefix}{name}"
        aliases = aliases if aliases else []

        arguments = []
        signature = inspect.signature(awaitable)
        for argname, param in signature.parameters.items():
            annotation = param.annotation
            arguments.append((argname, annotation))

        command = Command(
            name=name, function=awaitable, arguments=arguments, description=description, usage=usage, aliases=aliases
        )

        self.command_handlers[name] = command
        if aliases:
            for alias in aliases:
                self.command_handlers[alias] = command

        return awaitable

    async def _dispatch_event(self, event: str, args: tuple = None, kwargs: dict = None):
        """Dispatches the specified event with the provided arguments"""

        args = args if args else ()
        kwargs = kwargs if kwargs else {}

        if self.event_handlers.get(event):
            handlers = [event_handler(*args, **kwargs) for event_handler in self.event_handlers[event]]
            results = await asyncio.gather(*handlers, return_exceptions=True)

            for handler, result in zip(handlers, results):
                if isinstance(result, Exception):
                    self._logger.error(f"Exception occurred in {handler.__qualname__}:\n{format_exception(result)}")

    async def _dispatch_command(self, message):
        """Checks if a message is a command & parses it's arguments"""

        if self.case_sensitive:
            if not message.content.startswith(self.prefix):
                return
        else:
            if not message.content.lower().startswith(self.prefix.lower()):
                return

        split_command = message.content.strip().split()
        command_name = split_command[0].replace(self.prefix, "")
        split_arguments = split_command[1:]

        if self.case_sensitive:
            if not self.command_handlers.get(command_name):
                return
        else:
            if not {k.lower(): v for k, v in self.command_handlers.items()}.get(command_name.lower()):
                return

        command = self.command_handlers.get(command_name)
        number_of_args = len(command.arguments)

        if number_of_args - 1 > len(split_arguments):
            raise MissingRequiredArgument()

        ctx = Context(message, self, self.prefix, command_name)

        await command.function(ctx, *split_arguments[: number_of_args - 1])

    def run(self, token: str):
        """Runs the client with the provided token"""

        self._session = aiohttp.ClientSession()
        self._http = HTTPClient(self._session, self, token)
        self._websocket = WebSocketClient(self._session, self)
        self._loop.run_until_complete(self._websocket.connect(token=token, bot=self.bot))
