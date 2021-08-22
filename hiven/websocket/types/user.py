class User:
    def __init__(
        self, username: str, name: str, id: str, flags: str, icon: str = None, header: str = None
    ):
        self.username = username
        self.name = name
        self.id = id
        self.icon = icon
        self.header = header
        self.flags = flags
