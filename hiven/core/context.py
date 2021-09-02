class Context:
    def __init__(self, message, client, prefix, invoked_with):
        self.client = client
        self.message = message
        self.prefix = prefix
        self.invoked_with = invoked_with

        self.house = message.house
        self.room = message.room
        self.author = message.author

        self.send = self.room.send
