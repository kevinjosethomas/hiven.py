from hiven.client import Client


class DefaultPermissionOverrideSchema:
    allow: int
    deny: int


class DefaultPermissionOverride:
    def __init__(
        self, default_permission_override: DefaultPermissionOverrideSchema, client: Client
    ):
        self.allow = default_permission_override.get("allow")
        self.deny = default_permission_override.get("deny")
