from typing import List


from hiven.types.user import User
from hiven.types.member import Member
from hiven.types.attachment import Attachment


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
    def __init__(self, message: MessageSchema, client):
        self.id = message.get("id")
        self.room_id = message.get("room_id")
        self.house_id = message.get("house_id")
        self.content = message.get("content")
        self.attachment = (
            Attachment(message.get("attachment"), client) if message.get("attachment") else None
        )
        self.mentions = message.get("mentions")
        self.exploding = message.get("exploding")
        self.exploding_age = message.get("exploding_age")
        self.member = Member(message.get("member"), client)
        self.author_id = message.get("author_id")
        self.author = User(message.get("author"), client)
        self.device_id = message.get("device_id")
        self.bucket = message.get("bucket")
        self.timestamp = message.get("timestamp")

        self.house = client.houses.get(self.house_id)
        self.room = self.house.rooms.get(self.room_id) if self.house else None
