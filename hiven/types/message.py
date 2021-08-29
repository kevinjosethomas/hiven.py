from pprint import pprint
from typing import List

from .user import User
from .member import Member
from .attachment import Attachment


class MessageSchema:
    id: str
    room_id: str
    house_id: str
    content: str
    attachment: Attachment
    mentions: List[User]
    exploding: bool
    exploding_age: int
    member: Member
    author_id: str
    author: User
    device_id: str
    bucket: int
    timestamp: int


class Message:
    def __init__(self, message: MessageSchema):
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
        self.member = Member(message.get("member"))
        self.author_id = User(message.get("author_id"))
        self.author = message.get("author")
        self.device_id = message.get("device_id")
        self.bucket = message.get("bucket")
        self.timestamp = message.get("timestamp")
