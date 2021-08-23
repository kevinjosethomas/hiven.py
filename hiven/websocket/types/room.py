from .channel_emoji import ChannelEmoji
from ..schemas import Room as RoomSchema
from .default_permission_override import DefaultPermissionOverride


class Room:
    def __init__(self, room: RoomSchema):
        self.id = room.get("id")
        self.house_id = room.get("house_id")
        self.type = room.get("type")
        self.emoji = ChannelEmoji(room.get("emoji")) if room.get("emoji") else None
        self.name = room.get("name")
        self.position = room.get("position")
        self.last_message_id = room.get("last_message_id")
        self.description = room.get("description")
        self.default_permission_override = (
            DefaultPermissionOverride(room.get("default_permission_override"))
            if room.get("default_permission_override")
            else None
        )
