from fastapi import APIRouter
from schemas.books import CreateBook, UpdateBook, books
from services.books import BookCrud

books_router = APIRouter()
 
@books_router.get("/", status_code=200)
def get_all_books():
    return {"all books": list(books.values())}


@books_router.get("/{book_id}", status_code=200)
def get_book(book_id: int):
    BookCrud.get_book_by_id(book_id)
    

@books_router.post("/", status_code=201) 
def create_book(book: CreateBook):
    BookCrud.create_new_book(book)   


@books_router.patch("/{book_id}", status_code=200)
def update_book(book_id: int, book_data: UpdateBook):
    BookCrud.update_book_by_id(book_id, book_data)


@books_router.delete("/{book_id}", status_code=200)
def delete_book(book_id: int):
    BookCrud.delete_book_by_id(book_id)


@books_router.patch("/{book_id}/make unavailable", status_code=200)
def make_book_unavailable(book_id: int):
    BookCrud.mark_book_as_unavailable(book_id) 


@books_router.patch("/{book_id}/make available", status_code=200)
def make_book_available(book_id: int):
    BookCrud.mark_book_as_available(book_id)       
    