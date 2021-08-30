import json
import asyncio
import aiohttp
from enum import IntEnum

from hiven.data import WEBSOCKET_URL
from hiven.types import User, House, Message
from hiven.errors.websocket import WebSocketError


class OpCodes(IntEnum):
    SERVER = 0
    INIT = 1
    LOGIN = 2
    HEARTBEAT = 3


class WebSocketClient:
    def __init__(self, session: aiohttp.ClientSession, client):
        self._session = session
        self._client = client

        self._houses_event = asyncio.Event()

    async def init_state(self, data: dict):
        """Initialize bot's state"""

        self._client.user = User(data["user"], self._client)
        self._client._expected_houses_len = len(data.get("house_memberships", []))

        await self._houses_event.wait()

        self._client.is_ready = True
        await self._client.dispatch_event("ready")

    async def server_websocket_handler(self, msg: dict):
        """Handles websocket messages that arrive from the server"""

        self._client._logger.debug(f"Received event: {msg['e']}")

        if msg["e"] == "INIT_STATE":
            asyncio.create_task(self.init_state(msg["d"]))
        elif msg["e"] == "HOUSE_JOIN":
            self._client.houses[msg["d"]["id"]] = House(msg["d"], self._client)
            if len(self._client.houses) == self._client._expected_houses_len:
                self._houses_event.set()
        elif msg["e"] == "MESSAGE_CREATE":
            message = Message(msg["d"], self._client)
            await self._client.dispatch_event("message", (message,))

    async def connect(self, token: str, bot: bool = True):
        """Connects to the Hiven WebSocket Swarm"""

        self._token = token
        self._ws = await self._session.ws_connect(WEBSOCKET_URL)

        while True:
            msg = await self._ws.receive()

            if msg.type == aiohttp.WSMsgType.TEXT:

                message = json.loads(msg.data)

                if message["op"] == OpCodes.SERVER:
                    await self.server_websocket_handler(message)
                elif message["op"] == OpCodes.INIT:
                    await self._ws.send_json(
                        {"op": OpCodes.LOGIN, "d": {"token": ("Bot " if bot else "") + self._token}}
                    )
                    asyncio.create_task(self.heartbeat(message["d"]["hbt_int"] // 1000))
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                self._client._logger.debug("WebSocket connection was closed")
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                raise WebSocketError(msg)

    async def heartbeat(self, interval: int):
        """Start sending heartbeat websocket messages at the specified interval"""

        while True:
            self._client._logger.debug("Sending heartbeat...")
            await self._ws.send_json({"op": OpCodes.HEARTBEAT})
            await asyncio.sleep(interval)
