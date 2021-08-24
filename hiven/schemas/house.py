from typing import List

from .role import Role
from .room import Room
from .entity import Entity
from .member import Member


class House:
    id: str
    icon: str
    owner_id: str
    banner: str
    default_permissions: int
    rooms: List[Room]
    roles: List[Role]
    members: List[Member]
    entities: List[Entity]
