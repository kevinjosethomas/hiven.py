from hiven.schemas import DefaultPermissionOverride as DefaultPermissionOverrideSchema


class DefaultPermissionOverride:
    def __init__(self, default_permission_override: DefaultPermissionOverrideSchema):
        self.allow = default_permission_override.get("allow")
        self.deny = default_permission_override.get("deny")
