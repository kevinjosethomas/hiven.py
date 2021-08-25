from hiven.schemas import ChannelEmoji as ChannelEmojiSchema


class ChannelEmoji:
    def __init__(self, emoji: ChannelEmojiSchema):
        self.type = emoji.get("type")
        self.data = emoji.get("data")
