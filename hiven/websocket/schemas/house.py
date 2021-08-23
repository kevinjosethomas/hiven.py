from typing import List

from .room import Room
from .member import Member


class House:
    id: str
    name: str
    icon: str
    owner_id: str
    banner: str
    default_permissions: int
    members: List[Member]
    rooms: List[Room]
