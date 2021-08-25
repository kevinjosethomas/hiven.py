from hiven.schemas import PermissionOverride as PermissionOverrideSchema


class PermissionOverride:
    def __init__(self, permission_override: PermissionOverrideSchema):
        self.id = permission_override.get("id")
        self.type = permission_override.get("type")
        self.allow = permission_override.get("allow")
        self.deny = permission_override.get("deny")
