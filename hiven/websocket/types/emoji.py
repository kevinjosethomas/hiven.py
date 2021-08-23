from ..schemas import Emoji


class Emoji:
    def __init__(self, emoji: Emoji):
        self.type = emoji.type
        self.data = emoji.data
