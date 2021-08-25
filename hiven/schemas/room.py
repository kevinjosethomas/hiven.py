from typing import Dict

from hiven.schemas.channel_emoji import ChannelEmoji
from hiven.schemas.permission_override import PermissionOverride
from hiven.schemas.default_permission_override import DefaultPermissionOverride


class Room:
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
