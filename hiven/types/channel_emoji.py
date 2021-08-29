class ChannelEmojiSchema:
    type: int
    data: str


class ChannelEmoji:
    def __init__(self, emoji: ChannelEmojiSchema, client):
        self.type = emoji.get("type")
        self.data = emoji.get("data")
