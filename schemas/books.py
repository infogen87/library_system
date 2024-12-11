from pydantic import BaseModel
from typing import Optional

books = {}

class BookBase(BaseModel):
    id: int
    title: str
    author: str
    is_available: bool = True


class CreateBook(BookBase):
    pass


class UpdateBook(BookBase):
    id: Optional[int] = None
    title: Optional[str] = None
    author: Optional[str] = None 
   
