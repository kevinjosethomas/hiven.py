from typing import List

from hiven.schemas.role import Role
from hiven.schemas.room import Room
from hiven.schemas.entity import Entity
from hiven.schemas.member import Member


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
