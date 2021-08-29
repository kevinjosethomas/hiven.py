class PermissionOverrideSchema:
    id: str
    type: int
    allow: int
    deny: int


class PermissionOverride:
    def __init__(self, permission_override: PermissionOverrideSchema, client):
        self.id = permission_override.get("id")
        self.type = permission_override.get("type")
        self.allow = permission_override.get("allow")
        self.deny = permission_override.get("deny")
