
from schemas.users import users, User
from schemas.books import books, Book
from schemas.borrow_record import borrow_records, BorrowRecord, CreateBorrowRecord
from fastapi import HTTPException
import datetime
from uuid import uuid4





class BookRecordCrud:   

    @staticmethod
    def borrow_a_book(borrow_data: CreateBorrowRecord):
        user: User = users.get(borrow_data.user_id)
        book: Book = books.get(borrow_data.book_id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        if user.is_active == False:
            raise HTTPException(status_code=403, detail="user isn't active and can't borrow books")
        if not book:
            raise HTTPException(status_code=404, detail="book not found")
        if book.is_available == False:
            raise HTTPException(status_code=400, detail="this book isn't available for borrowing")
        book.is_available = False
        borrow_record_id = uuid4()
        borrow_book_data = BorrowRecord(id=borrow_record_id, **borrow_data.model_dump())
        borrow_records[borrow_record_id] = borrow_book_data
        return borrow_book_data


    @staticmethod
    def view_borrow_records_of_user(id_of_user: uuid4):
        user: User = users.get(id_of_user) 
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        user_borrow_record = {}
        for record in borrow_records:
            if record.user_id == user.id:
                # user_borrow_record_id = len(user_borrow_record) + 1
                user_borrow_record[len(user_borrow_record) + 1] = record
        return user_borrow_record
    

    @staticmethod
    def return_borrowed_book(book_id: int):
        book: Book = books.get(book_id)
        if not book:
            raise HTTPException(status_code=404, detail="book not found")
        if book.is_available == True:
            raise HTTPException(status_code=400, detail="book already returned,or was not borrwed")
        for record in borrow_records:
            if record.book_id == book_id:
                
                borrow_records[record.return_date] = datetime.now()
                book.is_available = True

            raise HTTPException(status_code=404, detail="this book was'nt borrowed!")
        return 
 




        

