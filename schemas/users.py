from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID, uuid4



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


users: dict[int, User] = {
    1: User(
        id=str(uuid4()),
        name="john",
        email="john@gmail.com",
        is_active=True
    ),
    2: User(
        id=str(uuid4()),
        name="sara",
        email="sara40@gmail.com",
        is_active=True
    ),
    3: User(
        id=str(uuid4()),
        name="ebitari",
        email="ebi@gmail.com",
        is_active=False  
    )}
