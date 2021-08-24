from typing import Coroutine
import aiohttp
import asyncio

from .websocket import WebSocketClient


AVAILABLE_EVENTS = ["ready"]


class Client:
    def __init__(self, bot: bool = True):
        self.bot = bot
        self._loop = asyncio.get_event_loop()

        self.event_handlers = {}
        self.commands = {}

        self.user = None
        self.houses = []

    def event(self, awaitable: Coroutine):
        """Decorator to recognize a function as an event handler"""

        print(awaitable.__name__)
        event_name = awaitable.__name__.replace("on_", "")
        if event_name not in AVAILABLE_EVENTS:
            print("invalid event")

        return awaitable

    def run(self, token: str):
        """Runs the client with the provided token"""

        self._session = aiohttp.ClientSession()
        self._websocket = WebSocketClient(self._session, self)
        self._loop.run_until_complete(self._websocket.connect(token=token, bot=self.bot))
