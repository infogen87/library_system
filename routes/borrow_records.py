from fastapi import APIRouter
from services.borrow_record import BookRecordCrud
from schemas.borrow_record import borrow_records


records_router = APIRouter()



@records_router.get("/", status_code=200)
def get_all_borrow_records():
    return {"all borrow records": {borrow_records}}


@records_router.get("/{user_id}/borrow-records")
def get_user_borrow_records(user_id: int):
    BookRecordCrud.view_borrow_records_of_user(user_id)


@records_router.post("/")
def borrow_book():
    pass


@records_router.patch("/")
def return_book():
    pass



