from typing import List
from datetime import datetime


from hiven.types.user import User


class MemberSchema:
    id: str
    user_id: str
    house_id: str
    user: User
    roles: List[str]
    presence: str
    last_permission_update: datetime
    joined_at: datetime


class Member:
    def __init__(self, member: MemberSchema, client):
        self.id = member.get("id")
        self.user_id = member.get("user_id")
        self.house_id = member.get("house_id")
        self.user = User(member.get("user"), client)
        self.roles = member.get("roles")
        self.presence = member.get("presence")
        self.last_permission_update = member.get("last_permission_update")
        self.joined_at = member.get("joined_at")
