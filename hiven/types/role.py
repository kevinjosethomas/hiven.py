class RoleSchema:
    id: str
    house_id: str
    name: str
    position: int
    level: int
    color: str
    allow: int
    deny: int


class Role:
    def __init__(self, role: RoleSchema, client):
        self.id = role.get("id")
        self.house_id = role.get("house_id")
        self.name = role.get("name")
        self.position = role.get("position")
        self.level = role.get("level")
        self.color = role.get("color")
        self.allow = role.get("allow")
        self.deny = role.get("deny")
