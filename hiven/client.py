import inspect
import aiohttp
import asyncio
import logging
from typing import Coroutine

from hiven.errors import EventHandlerError
from hiven.gateway import HTTPClient, WebSocketClient


AVAILABLE_EVENTS = ("ready", "message")


class Client:
    def __init__(self, bot: bool = True):
        self.bot = bot

        self._loop = asyncio.get_event_loop()
        self._logger = logging.getLogger("hiven")

        self.is_ready = False
        self._expected_houses_len = None

        self.event_handlers = {}
        self.commands = {}

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

    async def dispatch_event(self, event: str, args: tuple = (), kwargs: dict = {}):
        """Dispatches the specified event with the provided arguments"""

        if self.event_handlers.get(event):
            handlers = [
                event_handler(*args, **kwargs) for event_handler in self.event_handlers[event]
            ]
            await asyncio.gather(*handlers)

    def run(self, token: str):
        """Runs the client with the provided token"""

        self._session = aiohttp.ClientSession()
        self._http = HTTPClient(self._session, self, token)
        self._websocket = WebSocketClient(self._session, self)
        self._loop.run_until_complete(self._websocket.connect(token=token, bot=self.bot))
