from fastapi import APIRouter
from schemas.books import CreateBook, UpdateBook, books
from services.books import BookCrud
from uuid import UUID

books_router = APIRouter()
 
@books_router.get("/", status_code=200)
def get_all_books():
    return {"all books": list(books.values())}


@books_router.get("/{book_id}", status_code=200)
def get_book(book_id: UUID):
    book = BookCrud.get_book_by_id(book_id)
    return {"book": book}
    
    

@books_router.post("/", status_code=201) 
def create_book(book: CreateBook):
    BookCrud.create_new_book(book)
    return {"message": "book created successfully", "new book": book}   


@books_router.patch("/{book_id}", status_code=200)
def update_book(book_id: UUID, book_data: UpdateBook):
    book = BookCrud.update_book_by_id(book_id, book_data)
    return {"message": "book updated successfully", "updated book": book}


@books_router.delete("/{book_id}", status_code=200)
def delete_book(book_id: UUID):
    BookCrud.delete_book_by_id(book_id)
    return {"message": "book deleted successfully"}


@books_router.patch("/{book_id}/make_unavailable", status_code=200)
def make_book_unavailable(book_id: UUID):
    book = BookCrud.mark_book_as_unavailable(book_id) 
    return {"message": f"the book {book.title} is now unavailable!"}


@books_router.patch("/{book_id}/make_available", status_code=200)
def make_book_available(book_id: UUID):
    book = BookCrud.mark_book_as_available(book_id)  
    return {"message": f"the book {book.title} is now available!"}     
    