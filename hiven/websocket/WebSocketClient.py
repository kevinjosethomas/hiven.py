import json
import asyncio
import aiohttp
from pprint import pprint

from .types import User, House, Room


class WebSocketClient:
    def __init__(self, session: aiohttp.ClientSession, client):
        self._session = session
        self._client = client

    async def init_state(self, data: dict):
        """Initialize bot's state"""

        # pprint(data)

        self._client.user = User(
            username=data["user"].get("username"),
            name=data["user"].get("name"),
            id=data["user"].get("id"),
            flags=data["user"].get("flags"),
            icon=data["user"].get("icon"),
            header=data["user"].get("header"),
        )

    async def server_websocket_handler(self, msg: dict):
        """Handles websocket messages that arrive from the server"""

        print(msg["e"])

        if msg["e"] == "INIT_STATE":
            await self.init_state(msg["d"])
        elif msg["e"] == "HOUSE_JOIN":
            parsed_house = msg["d"]
            for index, room in enumerate(parsed_house["rooms"]):
                parsed_house["rooms"][index] = Room(room)

            pprint(parsed_house)

    async def connect(self, token: str, bot: bool = True):
        """Connects to the Hiven WebSocket Swarm"""

        self._token = token
        self._ws = await self._session.ws_connect(
            "wss://swarm.hiven.io/socket?encoding=json&compression=text_json"
        )

        while True:
            msg = await self._ws.receive()

            if msg.type == aiohttp.WSMsgType.TEXT:

                message = json.loads(msg.data)

                if message["op"] == 0:
                    await self.server_websocket_handler(message)
                elif message["op"] == 1:
                    await self._ws.send_json(
                        {"op": 2, "d": {"token": ("Bot " if bot else "") + self._token}}
                    )
                    asyncio.create_task(self.heartbeat(message["d"]["hbt_int"] // 1000))
            elif msg.type == aiohttp.WSMsgType.CLOSE:
                print("closing")
                print(msg)
            elif msg.type == aiohttp.WSMsgType.CLOSED:
                print("closed")
                print(msg)
                break
            elif msg.type == aiohttp.WSMsgType.ERROR:
                print("error")
                print(msg)
                print("\n\n")
                break

    async def heartbeat(self, interval: int):
        """Start sending heartbeat websocket messages at the specified interval"""

        while True:
            print("sending heartbeat...")
            await self._ws.send_json({"op": 3})
            await asyncio.sleep(interval)
