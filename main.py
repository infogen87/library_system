from fastapi import FastAPI
from routes.users import users_router
from routes.books import books_router
from routes.borrow_records import records_router

app = FastAPI(title="E-Library API System",
              description="An API for managing an online library system.",)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(records_router, prefix="/borrow_records", tags=["book_records"])

@app.get("/")
def home():
    return {"message": "welcome to my e-library api system!"}