import aiohttp
import asyncio

from .websocket import WebSocketClient


class Client:
    def __init__(self, bot: bool = True):
        self.bot = bot
        self._loop = asyncio.get_event_loop()

    def run(self, token: str):
        """Runs the client with the provided token"""

        self._session = aiohttp.ClientSession()
        self._websocket = WebSocketClient(self._session, self)
        self._loop.run_until_complete(self._websocket.connect(token=token, bot=self.bot))
