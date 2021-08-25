from ..schemas import Message
from .attachment import Attachment


class Message:
    def __init__(self, message: Message):
        self.id = message.get("id")
        self.room_id = message.get("room_id")
        self.house_id = message.get("house_id")
        self.content = message.get("content")
        self.attachment = (
            Attachment(message.get("attachment")) if message.get("attachment") else None
        )
        self.mentions = message.get("mentions")
        self.exploding = message.get("exploding")
        self.exploding_age = message.get("exploding_age")
        self.member = message.get("member")
        self.author_id = message.get("author_id")
        self.author = message.get("author")
        self.device_id = message.get("device_id")
        self.bucket = message.get("bucket")
        self.timestamp = message.get("timestamp")
