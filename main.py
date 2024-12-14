from fastapi import FastAPI
from routes.users import users_router
from routes.books import books_router
from routes.borrow_records import records_router

app = FastAPI()

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(records_router, prefix="/borrow_records", tags=["book_records"])

@app.get("/")
def home():
    return {"message": "welcome to my e-library api system!"}



# Project Title:
# E-Library API System

# Description:
# The goal of this project is to create a simple API for managing an online library system. This system allows users to borrow and return books, manage user information, and track the availability of books.

# The system includes the following entities:

# User: Represents a user of the library.
# id: Unique identifier for the user.
# name: Name of the user.
# email: Email address of the user.
# is_active: Indicates if the user account is active (defaults to True).
# Book: Represents a book in the library.
# id: Unique identifier for the book.
# title: Title of the book.
# author: Author of the book.
# is_available: Indicates if the book is available for borrowing (defaults to True).
# BorrowRecord: Represents a borrowing record.
# id: Unique identifier for the record.
# user_id: ID of the user who borrowed the book.
# book_id: ID of the borrowed book.
# borrow_date: Date the book was borrowed.
# return_date: Date the book was returned (if applicable).
# Requirements:
# API Endpoints:
# You are required to create the following endpoints:

# User Endpoints:
# CRUD operations for User.
# Endpoint to deactivate a user, setting is_active to False.
# Book Endpoints:
# CRUD operations for Book.
# Endpoint to mark a book as unavailable (e.g., if it’s lost or under maintenance).
# Borrow Operations:
# Borrow a book:
# Allows an active user to borrow an available book.
# A user cannot borrow a book if it’s unavailable or if they have already borrowed the same book.
# If the book is successfully borrowed, update its is_available status to False.
# If the book cannot be borrowed, return an appropriate response and status code.
# Return a book:
# Marks a borrowed book as returned by updating the return_date in the BorrowRecord and setting the book’s is_available status to True.
# Borrow Record Management:
# Endpoint to view borrowing records for a specific user.
# Endpoint to view all borrowing records.
# Additional Requirements:
# Database:
# Use in-memory data structures (list or dict) for storage.
# Validation:
# Use Pydantic models to validate inputs for all endpoints.
# Code Structure:
# Follow a modular structure for better readability and maintainability.
# Use separate files for models, routes, and application configuration.
# Status Codes:
# Use appropriate HTTP status codes for success and error scenarios.



# Constraints:
# Users must be active to perform any operations.
# Books must be available to be borrowed.
# Each borrowing operation should have a unique BorrowRecord.
# Submission Instructions:
# Develop the project using FastAPI.
# Add a README.md file with instructions on how to run the application.
# Push your code to a public GitHub repository.
# Include test cases to validate your API endpoints (optional for extra credit).
