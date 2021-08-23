from ..schemas import Emoji


class ChannelEmoji:
    def __init__(self, emoji: Emoji):
        self.type = emoji.type
        self.data = emoji.data
