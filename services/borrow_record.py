
from schemas.users import users, User
from schemas.books import books, Book
from schemas.borrow_record import borrow_records, BorrowRecord
from fastapi import HTTPException
import datetime





class BookRecordCrud:
    @staticmethod
    def borrow_a_book(user_id: int, book_id: int):
        user: User = users.get(user_id)
        book: Book = books.get(book_id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        if user.is_active == False:
            raise HTTPException(status_code=403, detail="user isn't active and can't borrow books")
        if not book:
            raise HTTPException(status_code=404, detail="book not found")
        if book.is_available == False:
            raise HTTPException(status_code=400, detail="this book has already been borrowed")
        book.is_available = False
        borrow_record_id = len(borrow_records) + 1
        borrow_record = BorrowRecord(id=borrow_record_id, user_id=user.id, book_id=book.id, borrow_date=datetime.now())
        borrow_records[borrow_record_id] = borrow_record
        return borrow_record
       

    @staticmethod
    def view_borrow_records_of_user(id_of_user: int):
        user: User = users.get(id_of_user) 
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        user_borrow_record = {}
        for record in borrow_records:
            if record.user_id == user.id:
                user_borrow_record_id = len(user_borrow_record) + 1
                user_borrow_record[user_borrow_record_id] = record
        return user_borrow_record
    

    @staticmethod
    def return_borrowed_book(returned_book_id: int):
        book: Book = books.get(returned_book_id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found")
        if book.is_available == True:
            raise HTTPException(status_code=400, detail="book already returned")
        for record in borrow_records:
            if record.book_id == returned_book_id:

                borrow_records[record.return_date] = datetime.now()
                book.is_available = True

            raise HTTPException(status_code=404, detail="this book wasnt borrowed!")

 




        

