class UserSchema:
    id: str
    username: str
    name: str
    flags: int
    icon: str
    header: str
    bio: str
    website: str
    location: str
    application: str


class User:
    def __init__(self, user: UserSchema, client):
        self.id = user.get("id")
        self.username = user.get("username")
        self.name = user.get("name")
        self.flags = user.get("flags")
        self.icon = user.get("icon")
        self.header = user.get("header")
        self.bio = user.get("bio")
        self.website = user.get("website")
        self.location = user.get("location")
        self.application = user.get("application")
