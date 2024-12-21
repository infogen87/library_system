Library System API

Description:

The E-Library API System is a simple API designed to manage an online library. It allows users to:  
1. Borrow and return books.  
2. Manage user information.  
3. Track the availability of books.

project uses FastAPI to provide a modular and maintainable backend API.



The system consists of three entities:  
1. User: Represents library users.  
2. Book: Represents books in the library.  
3. BorrowRecord: Represents borrowing history.  



Features  
User Management  
- CRUD operations for users.  
- Deactivate users by setting `is_active` to `False`.
- Activate users by setting `is_active` to `True`. 

Book Management  
- CRUD operations for books.  
- Mark books as unavailable (e.g., lost or under maintenance).  
- Mark books as available

Borrow and Return Books  
- Allow active users to borrow available books.  
- Prevent users from borrowing unavailable books or borrowing the same book twice.  
- Update the book's availability status upon borrowing or returning.  
- Track borrow and return dates in the borrowing records.

Borrow Record Management  
- View borrowing records for specific users.  
- View all borrowing records.



Technologies Used  
- FastAPI: For creating the RESTful API.  
- Pydantic: For data validation.  
- Datetime: To manage dates for borrowing and returning books.  
- UUID: For generating unique identifiers.  
- Python: The programming language used for the project.



Installation  

1. Clone the repository

   git clone https://github.com/infogen87/library_system.git
   cd library_system


2. Set up a virtual environment 

   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`


3. Install the dependencies

   pip install fastapi[all]
   

4. Run the API server  

   uvicorn main:app --reload
  

The API will be available at `http://127.0.0.1:8000`.



Usage  

Example Endpoints  

User Management  
- Create a user:  
  `POST /users`  
  Request body:  

  {
    "name": "John Doe",
    "email": "john.doe@example.com"
  }
 

- Deactivate a user:  
  `PUT /users/{user_id}/deactivate`  

Book Management  
- Add a book:  
  `POST /books`  
  Request body:  

  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
  }


- Mark a book as unavailable:  
  `PUT /books/{book_id}/make_unavailable`  

Borrow Operations  
- Borrow a book:  
  `POST /borrow_records`  
  Request body:  
 
  {
    "user_id": "123",
    "book_id": "456"
  }


- Return a book:  
  `PUT /borrow_records/{book_id}/return_book`  

View Borrow Records  
- For a specific user:  
  `GET /borrow_records/{user_id}/borrow_records`
    
- All records:  
  `GET /borrow_records`  

