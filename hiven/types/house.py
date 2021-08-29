from typing import List


from hiven.types.role import Role
from hiven.types.room import Room
from hiven.types.member import Member
from hiven.types.entity import Entity


class HouseSchema:
    id: str
    icon: str
    owner_id: str
    banner: str
    default_permissions: int
    rooms: List[Room]
    roles: List[Role]
    members: List[Member]
    entities: List[Entity]


class House:
    def __init__(self, house: HouseSchema, client):
        self.id = house.get("id")
        self.name = house.get("name")
        self.icon = house.get("icon")
        self.owner_id = house.get("owner_id")
        self.banner = house.get("banner")
        self.default_permissions = house.get("default_permissions")
        self.members = []
        self.rooms = {}
        self.entities = []

        for member in house["members"]:
            self.members.append(Member(member, client))

        for room in house["rooms"]:
            self.rooms[room["id"]] = Room(room, client)

        for entity in house["entities"]:
            self.entities.append(Entity(entity, client))
