from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import UUID





class BorrowRecordBase(BaseModel):
    user_id: UUID
    book_id: UUID
    borrow_date: date
    return_date: date



class BorrowRecord(BorrowRecordBase):
    id: UUID


class CreateBorrowRecord(BorrowRecordBase):
    borrow_date: Optional[date] = date.today()
    return_date: Optional[date] = None
    

borrow_records: dict[int: BorrowRecord] = {}
