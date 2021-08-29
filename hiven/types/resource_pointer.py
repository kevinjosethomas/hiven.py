class ResourcePointerSchema:
    resource_id: str
    resource_type: str


class ResourcePointer:
    def __init__(self, resource_pointer: ResourcePointerSchema, client):
        self.resource_id = resource_pointer.get("resource_id")
        self.resource_type = resource_pointer.get("resource_type")
