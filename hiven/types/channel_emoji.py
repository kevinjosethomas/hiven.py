from hiven.client import Client


class ChannelEmojiSchema:
    type: int
    data: str


class ChannelEmoji:
    def __init__(self, emoji: ChannelEmojiSchema, client: Client):
        self.type = emoji.get("type")
        self.data = emoji.get("data")
