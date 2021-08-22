from datetime import date, datetime

from .user import User


class Member:
    id: str
    user_id: str
    house_id: str
    user: User
    roles: list[str]
    presence: str
    last_permission_update: datetime
    joined_at: datetime
