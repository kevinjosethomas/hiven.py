from .channel_emoji import ChannelEmoji
from ..schemas import Room as RoomSchema


class Room:
    def __init__(self, room: RoomSchema):
        self.id = room.get("id")
        self.house_id = room.get("house_id")
        self.type = room.get("type")
        self.emoji = ChannelEmoji(room.get("emoji"))
        self.name = room.get("name")
        self.position = room.get("position")
        self.last_message_id = room.get("last_message_id")
        self.description = room.get("description")
        self.default_permission_override = room.get("default_permission_override")
