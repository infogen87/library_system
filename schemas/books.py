from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4

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

 


   

books: dict[int, Book] = {
    1: Book(
        id=str(uuid4()),
        title="The Catcher in the Rye",
        author="J.D. Salinger",
        is_available=True
    ),
    2: Book(
        id=str(uuid4()),
        title="To Kill a Mockingbird",
        author="Harper Lee",
        is_available=True
    ),
    3: Book(
        id=str(uuid4()),
        title="1984",
        author="George Orwell",
        is_available=False  
    )  
    
}
