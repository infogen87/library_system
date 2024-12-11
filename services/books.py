from schemas.books import books, CreateBook, UpdateBook
from fastapi import HTTPException
class BookCrud:
    @staticmethod
    def get_book_by_id(id: int):
        book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        return {"book": {book}}
    

    @staticmethod
    def create_new_book(book_data: CreateBook):
        book_id = len(books) + 1
        book = {"id": book_id, **book_data.model_dump()}
        books[book_id] = book
        return {"message": "book created successfully!", "new book": {book}}


    @staticmethod
    def update_book_by_id(id: int, book_data: UpdateBook):
        book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        book.id = book_data.id
        book.name = book_data.name
        book.email = book_data.email
        return {"updated book": {book}, "message": "book updated successfully"}


    @staticmethod
    def delete_book_by_id(id: int):
        book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        del books[book]
        return {"message": "book deleted successfully"}
