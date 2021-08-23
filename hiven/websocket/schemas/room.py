from .channel_emoji import ChannelEmoji
from .permission_override import PermissionOverride


class Room:
    id: str
    house_id: str
    type: int
    emoji: ChannelEmoji
    name: str
    position: int
    last_message_id: str
    description: str
    default_permission_override: PermissionOverride
