from ..schemas import ChannelEmoji


class ChannelEmoji:
    def __init__(self, emoji: ChannelEmoji):
        self.type = emoji.type
        self.data = emoji.data
