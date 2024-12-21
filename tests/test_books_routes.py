import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"


def test_get_book_by_id():
    create_response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "Test Author"}
    )
    book_id = create_response.json()["id"]

    response = client.get(f"/books/{book_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    assert data["title"] == "Test Book"
    assert data["author"] == "Test Author"


def test_get_all_books():
    client.post("/books/", json={"title": "Book1", "author": "Author1"})
    client.post("/books/", json={"title": "Book2", "author": "Author2"})

    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_update_book():
    create_response = client.post(
        "/books/",
        json={"title": "Original Title", "author": "Original Author"}
    )
    book_id = create_response.json()["id"]

    update_response = client.put(
        f"/books/{book_id}",
        json={"title": "Updated Title", "author": "Updated Author"}
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["title"] == "Updated Title"
    assert data["author"] == "Updated Author"

    fetch_response = client.get(f"/books/{book_id}")
    assert fetch_response.status_code == 200
    fetch_data = fetch_response.json()
    assert fetch_data["title"] == "Updated Title"
    assert fetch_data["author"] == "Updated Author"


def test_delete_book():
    create_response = client.post(
        "/books/",
        json={"title": "Book to Delete", "author": "Delete Author"}
    )
    book_id = create_response.json()["id"]

    delete_response = client.delete(f"/books/{book_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Book deleted successfully"}

    fetch_response = client.get(f"/books/{book_id}")
    assert fetch_response.status_code == 404
    assert fetch_response.json() == {"detail": "Book not found"}
