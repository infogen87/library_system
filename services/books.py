from schemas.books import books, Book, CreateBook, UpdateBook
from fastapi import HTTPException
class BookCrud:
    @staticmethod
    def get_book_by_id(id: int):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        return {"book": book}
    

    @staticmethod
    def create_new_book(book_data: CreateBook):
        book_id = len(books) + 1
        book = Book(id=book_id, **book_data.model_dump())
        books[book_id] = book
        return {"message": "book created successfully", "new book": book}
        
        

    @staticmethod
    def update_book_by_id(id: int, book_data: UpdateBook):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        for k, v in book_data.model_dump().items():
            setattr(book, k, v)
        return {"message": "book updated successfully", "updated book": book}


    @staticmethod
    def delete_book_by_id(id: int):
        book: Book = books.get(id)
        if book not in books:
            raise HTTPException(status_code=404, detail="book not found!")
        del books[id]
        return {"message": "book deleted successfully"}



    @staticmethod
    def mark_book_as_unavailable(id: int):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        if book.is_available == False:
            raise HTTPException(status_code=400, detail="book already unavailable!")
        book.is_available = False
        return {"message": f"the book {book.title} is now unavailable!"}
    

    @staticmethod
    def mark_book_as_available(id: int):
        book: Book = books.get(id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found!")
        if book.is_available == True:
            raise HTTPException(status_code=400, detail="book is already available!")
        book.is_available = True
        return {"message": f"the book {book.title} is now available!"}
