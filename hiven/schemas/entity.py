from typing import List

from hiven.schemas.resource_pointer import ResourcePointer


class Entity:
    id: str
    house_id: str
    name: str
    position: int
    type: int
    resource_pointers: List[ResourcePointer]
