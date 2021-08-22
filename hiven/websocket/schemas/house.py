from .room import Room
from .member import Member


class House:
    id: str
    name: str
    icon: str
    owner_id: str
    default_permissions: int
    members: list[Member]
    rooms: list[Room]
    banner: str