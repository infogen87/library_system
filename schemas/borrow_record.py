from pydantic import BaseModel


class BorrowRecord(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: 