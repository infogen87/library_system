
from schemas.users import users, User
from schemas.books import books, Book
from schemas.borrow_record import borrow_records, BorrowRecord, CreateBorrowRecord
from fastapi import HTTPException
from datetime import date
from uuid import UUID, uuid4





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
    def get_borrow_records_by_user(user_id: UUID):
        user: User = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")
        user_records = []
        for record_id, record in borrow_records.items():
            if record.user_id == user_id:
                user_records.append(record_id)
        if not user_records:
            raise HTTPException(status_code=404, detail="User has no borrow records.")
        else:
            return user_records  
            
            
    def get_borrow_records_by_user(user_id: UUID):
        user = users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found")

        user_records = [record_id for record_id, record in borrow_records.items() if record.user_id == user_id]

        if not user_records:
            raise HTTPException(status_code=404, detail="User has no borrow records.")

        return user_records
        
    



    @staticmethod
    def return_borrowed_book(id_of_book: UUID):
        book: Book = books.get(id_of_book)
        if not book:
            raise HTTPException(status_code=404, detail="book not found")
        for record in borrow_records.items():
            if record["book_id"] == id_of_book:
                book.is_available = True
                record["return_date"] = date.today()
                return record
            raise HTTPException(status_code=404, detail="book has wasnt borrowed")
           
        
        

        




 




        

