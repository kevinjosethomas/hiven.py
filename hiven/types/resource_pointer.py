from ..schemas import ResourcePointer as ResourcePointerSchema


class ResourcePointer:
    def __init__(self, resource_pointer: ResourcePointerSchema):
        self.resource_id = resource_pointer.get("resource_id")
        self.resource_type = resource_pointer.get("resource_type")
