from hiven.schemas import Role as RoleSchema


class Role:
    def __init__(self, role: RoleSchema):
        self.id = role.get("id")
        self.house_id = role.get("house_id")
        self.name = role.get("name")
        self.position = role.get("position")
        self.level = role.get("level")
        self.color = role.get("color")
        self.allow = role.get("allow")
        self.deny = role.get("deny")
