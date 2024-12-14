from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    is_available: bool = True


class Book(BookBase):
    id: int    


class CreateBook(BookBase):
    is_available: Optional[bool] = True


class UpdateBook(BookBase):
    title: Optional[str] = None
    author: Optional[str] = None
    is_available: Optional[bool] = True 


books: dict[int:Book] = {}    
   
