from typing import Dict


from hiven.types.channel_emoji import ChannelEmoji
from hiven.types.permission_override import PermissionOverride
from hiven.types.default_permission_override import DefaultPermissionOverride


class RoomSchema:
    id: str
    house_id: str
    type: int
    emoji: ChannelEmoji
    name: str
    position: int
    last_message_id: str
    description: str
    permission_overrides: Dict[str, PermissionOverride]
    default_permission_override: DefaultPermissionOverride


class Room:
    def __init__(self, room: RoomSchema, client):
        self._client = client

        self.id = room.get("id")
        self.house_id = room.get("house_id")
        self.type = room.get("type")
        self.emoji = ChannelEmoji(room.get("emoji"), client) if room.get("emoji") else None
        self.name = room.get("name")
        self.position = room.get("position")
        self.last_message_id = room.get("last_message_id")
        self.description = room.get("description")
        self.default_permission_override = (
            DefaultPermissionOverride(room.get("default_permission_override"), client)
            if room.get("default_permission_override")
            else None
        )
        self.permission_overrides = {}

        if room.get("permission_overrides"):
            for id, permission_override in room.get("permission_overrides").items():
                self.permission_overrides[id] = PermissionOverride(permission_override, client)

    async def send(self, message: str):
        """Sends a message in the defined room"""

        response, data = await self._client._http.request(
            method="POST", endpoint=f"/rooms/{self.id}/messages", data={"content": message}
        )

        return True
