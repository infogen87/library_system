from pydantic import BaseModel
from typing import Optional

users = {}

class UserBase(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True



class CreateUser(UserBase):
    id: 


class UpdateUser(UserBase):
    id: Optional[int] = None 
    name: Optional[str] = None
    email: Optional[str] = None



