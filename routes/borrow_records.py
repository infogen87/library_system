from fastapi import APIRouter, status
from services.borrow_record import BookRecordCrud
from schemas.borrow_record import borrow_records


records_router = APIRouter()



@records_router.get("/", status_code=200)
def get_all_borrow_records():
    return {"all borrow records": list(borrow_records.values())}


@records_router.get("/{user_id}/borrow-records", status_code=status.HTTP_200_OK)
def get_user_borrow_records(user_id: int):
    BookRecordCrud.view_borrow_records_of_user(user_id)


@records_router.post("/", status_code=status.HTTP_201_CREATED)
def borrow_book(user_id: int, book_id: int):
    borrow_record = BookRecordCrud.borrow_a_book(user_id, book_id)
    return {"message": "book successfully borrowed", "new borrow record": borrow_record}


@records_router.patch("/")
def return_book():
    pass



