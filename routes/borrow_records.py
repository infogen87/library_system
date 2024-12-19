from fastapi import APIRouter, status
from services.borrow_record import BookRecordCrud
from schemas.borrow_record import borrow_records, CreateBorrowRecord
from uuid import UUID

records_router = APIRouter()



@records_router.get("/", status_code=200)
def get_all_borrow_records():
    return {"all borrow records": list(borrow_records.values())}


@records_router.get("/{user_id}/borrow_records", status_code=status.HTTP_200_OK)
def get_user_borrow_records(user_id: UUID):
    BookRecordCrud.view_borrow_records_of_user(user_id)

 
@records_router.post("/", status_code=201)
def borrow_book(borrow_book_data: CreateBorrowRecord):
    BookRecordCrud.borrow_a_book(borrow_book_data)
    return {"message": "book successfully borrowed", "new borrow record": borrow_book_data}


@records_router.patch("/{book_id}/return_book")
def return_book():
    pass



