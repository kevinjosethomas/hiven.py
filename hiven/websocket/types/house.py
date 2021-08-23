from .room import Room
from ..schemas import House as HouseSchema


class House:
    def __init__(self, house: HouseSchema):
        self.id = house.get("id")
        self.name = house.get("name")
        self.icon = house.get("icon")
        self.owner_id = house.get("owner_id")
        self.banner = house.get("banner")
        self.default_permissions = house.get("default_permissions")
        self.members = house.get("members")
        self.rooms = []

        for room in house["rooms"]:
            self.rooms.append(Room(room))
