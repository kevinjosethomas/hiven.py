from .room import Room
from .member import Member
from .entity import Entity
from ..schemas import House as HouseSchema


class House:
    def __init__(self, house: HouseSchema):
        self.id = house.get("id")
        self.name = house.get("name")
        self.icon = house.get("icon")
        self.owner_id = house.get("owner_id")
        self.banner = house.get("banner")
        self.default_permissions = house.get("default_permissions")
        self.members = []
        self.rooms = []
        self.entities = []

        for member in house["members"]:
            self.members.append(Member(member))

        for room in house["rooms"]:
            self.rooms.append(Room(room))

        for entity in house["entities"]:
            self.entities.append(Entity(entity))
