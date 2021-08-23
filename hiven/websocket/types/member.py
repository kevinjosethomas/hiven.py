from .user import User
from ..schemas import Member as MemberSchema


class Member:
    def __init__(self, member: MemberSchema):
        self.id = member.get("id")
        self.user_id = member.get("user_id")
        self.house_id = member.get("house_id")
        self.user = User(member.get("user"))
        self.roles = member.get("roles")
        self.presence = member.get("presence")
        self.last_permission_update = member.get("last_permission_update")
        self.joined_at = member.get("joined_at")
