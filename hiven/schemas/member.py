from typing import List
from datetime import datetime

from hiven.schemas.user import User


class Member:
    id: str
    user_id: str
    house_id: str
    user: User
    roles: List[str]
    presence: str
    last_permission_update: datetime
    joined_at: datetime
