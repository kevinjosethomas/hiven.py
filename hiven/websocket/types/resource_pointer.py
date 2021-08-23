from ..schemas import ResourcePointer


class ResourcePointer:
    def __init__(self, resource_pointer: ResourcePointer):
        self.resource_id = resource_pointer.get("resource_id")
        self.resource_type = resource_pointer.get("resource_type")
