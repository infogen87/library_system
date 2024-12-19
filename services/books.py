from schemas.books import books, Book, CreateBook, UpdateBook
from uuid import UUID, uuid4
from fastapi import HTTPException


class BookCrud:
    @staticmethod
    def get_book_by_id(id: UUID):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        return book
    

    @staticmethod
    def create_new_book(book_data: CreateBook):
        book_id = uuid4()
        book = Book(id=book_id, **book_data.model_dump())
        books[book_id] = book
        return book
        
        

    @staticmethod
    def update_book_by_id(id: UUID, book_data: UpdateBook):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        for k, v in book_data.model_dump().items():
            setattr(book, k, v)
        return book


    @staticmethod
    def delete_book_by_id(book_id: UUID):
        if book_id not in books:
            raise HTTPException(status_code=404, detail="book not found!")
        del books[book_id]
        return


    @staticmethod
    def mark_book_as_unavailable(id: UUID):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        if book.is_available == False:
            raise HTTPException(status_code=400, detail="book already unavailable!")
        book.is_available = False
        return book
    

    @staticmethod
    def mark_book_as_available(id: UUID):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        if book.is_available == True:
            raise HTTPException(status_code=400, detail="book is already available!")
        book.is_available = True
        return book
