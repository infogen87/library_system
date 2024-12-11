from fastapi import APIRouter
from schemas.books import CreateBook, UpdateBook, books
from services.books import BookCrud

book_router = APIRouter()
 
@book_router.get("/")
def get_all_books():
    return {"all books": {books}}


@book_router.get("/{book_id}")
def get_book(book_id: int):
    BookCrud.get_book_by_id(book_id)
    

@book_router.post("/") 
def create_book(book: CreateBook):
    BookCrud.create_new_book(book)   


@book_router.patch("/{book_id}")
def update_book(book_id: int, book_data: UpdateBook):
    BookCrud.update_book_by_id(book_id, book_data)


@book_router.delete("/{book_id}")
def delete_book(book_id: int):
    BookCrud.delete_book_by_id(book_id)
    