from pydantic import BaseModel
from datetime import date
from typing import Optional




class BorrowRecordBase(BaseModel):
    user_id: int
    book_id: int
    borrow_date: date
    return_date: Optional[date] = None


class BorrowRecord(BorrowRecordBase):
    id: int


class CreateBorrowRecord(BorrowRecordBase):
    pass
    




borrow_records: dict[int: BorrowRecord] = {}
