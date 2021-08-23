from ..schemas import ChannelEmoji


class ChannelEmoji:
    def __init__(self, emoji: ChannelEmoji):
        self.type = emoji.get("type")
        self.data = emoji.get("data")
