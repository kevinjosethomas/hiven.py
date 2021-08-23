from .emoji import Emoji
from .permission_override import PermissionOverride


class Room:
    id: str
    house_id: str
    type: int
    emoji: Emoji
    name: str
    position: int
    last_message_id: str
    description: str
    default_permission_override: PermissionOverride
