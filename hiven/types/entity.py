from hiven.schemas import Entity as EntitySchema
from hiven.types.resource_pointer import ResourcePointer


class Entity:
    def __init__(self, entity: EntitySchema):
        self.id = entity.get("id")
        self.house_id = entity.get("house_id")
        self.name = entity.get("name")
        self.position = entity.get("position")
        self.type = entity.get("type")
        self.resource_pointers = []

        for resource_pointer in entity["resource_pointers"]:
            self.resource_pointers.append(ResourcePointer(resource_pointer))
