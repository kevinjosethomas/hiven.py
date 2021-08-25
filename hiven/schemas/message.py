from typing import List

from .user import User
from .member import Member
from .attachment import Attachment


class Message:
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
