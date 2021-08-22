from .emoji import Emoji
from .permission_override import PermissionOverride


class Room:
    type: int
    position: int
    name: str
    last_message_id: str
    id: str
    house_id: str
    emoji: Emoji
    description: str
    default_permission_override: PermissionOverride
