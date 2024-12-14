
from schemas.users import users, UserBase
from schemas.books import BookBase, books
from schemas.borrow_record import borrow_records
from fastapi import HTTPException





class BookRecordCrud:
    


    @staticmethod
    def borrow_book(user_id: int, book_id: int):
        user: UserBase = users.get(user_id)
        book: BookBase = books.get(book_id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        if user.is_active == False:
            raise HTTPException(status_code=403, detail="user isn't active and can't borrow books")
        if book.is_available == False:
            raise HTTPException(status_code=404, detail="this book has been borrowed")
        borrow_record_id = len(borrow_records) + 1

        # new_borrow_record = {
        #     "id": borrow_record_id,
        #     "user_id": 
        # }
        # book.is_available = False
        # return {"message": "the book {book.title} has been borrowed successfully", "borrow_record":  }
    

    # @staticmethod
    # def return_book()
        

    @staticmethod
    def view_borrow_records_of_user(id_of_user: int):
        user = users.get(id_of_user) 
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        user_borrow_record = {}
        for record in borrow_records:
            if record.user_id == id_of_user:
                user_borrow_record[record.id] = record
        return {"users borrow records": user_borrow_record}        



        

