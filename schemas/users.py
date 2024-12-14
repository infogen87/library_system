from pydantic import BaseModel
from typing import Optional



class UserBase(BaseModel):
    name: str
    email: str
    is_active: bool = True


class User(UserBase):
    id: int


class CreateUser(UserBase):
    is_active: Optional[bool] = True



class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None


users: dict[int: User] = {}
