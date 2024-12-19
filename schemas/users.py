from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID



class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True


class User(UserBase):
    id: UUID


class CreateUser(UserBase):
    is_active: Optional[bool] = True



class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None


users: dict[int: User] = {}
