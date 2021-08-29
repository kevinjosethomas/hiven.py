class DefaultPermissionOverrideSchema:
    allow: int
    deny: int


class DefaultPermissionOverride:
    def __init__(self, default_permission_override: DefaultPermissionOverrideSchema, client):
        self.allow = default_permission_override.get("allow")
        self.deny = default_permission_override.get("deny")
