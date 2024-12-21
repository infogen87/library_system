from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import UUID, uuid4





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
    

borrow_records: dict[int, BorrowRecord] = {
    # 1: BorrowRecord(
    #     user_id=str(uuid4()),
    #     book_id=str(uuid4()),
    #     borrow_date=date.today(),
    #     return_date=date.today()
    # ),
    # 2: BorrowRecord(
    #     user_id=str(uuid4()),
    #     book_id=str(uuid4()),
    #     borrow_date=date.today(),
    #     return_date=date.today()
    # ),
    # 3: BorrowRecord(
    #     user_id=str(uuid4()),
    #     book_id=str(uuid4()),
    #     borrow_date=date.today(),
    #     return_date=date.today()  
    # )
}
