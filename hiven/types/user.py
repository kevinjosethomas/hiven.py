from hiven.schemas import User as UserSchema


class User:
    def __init__(self, user: UserSchema):
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
