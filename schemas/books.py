from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True


class Book(BookBase):     
    id: UUID

class CreateBook(BookBase):
    is_available: Optional[bool] = True


class UpdateBook(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    is_available: Optional[bool] = None 


books: dict[int: Book] = {}    
   
  