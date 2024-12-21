import pytest
from fastapi.testclient import TestClient
from main import app
from uuid import uuid4
from datetime import date

client = TestClient(app)

valid_user_id = uuid4()
valid_book_id = uuid4()
invalid_user_id = uuid4()
invalid_book_id = uuid4()


@pytest.fixture(scope="module", autouse=True)
def setup_data():
    client.post("/users/", json={
        "name": "Test User",
        "email": "testuser@example.com",
        "is_active": True
    })

    client.post("/books/", json={
        "title": "Test Book",
        "author": "Test Author",
        "is_available": True
    })

    client.post("/borrow_records/", json={
        "user_id": str(valid_user_id),
        "book_id": str(valid_book_id),
        "borrow_date": str(date.today()),
        "return_date": None
    })


def test_get_borrow_records_success():
    response = client.get(f"/borrow-records/{valid_user_id}")
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert "user_records" in data
    assert len(data["user_records"]) > 0


def test_get_borrow_records_user_not_found():
    response = client.get(f"/borrow-records/{invalid_user_id}")
    print(response.json())
    assert response.status_code == 404


def test_get_borrow_records_no_records():
    another_user_id = uuid4()
    client.post("/users/", json={
        "name": "Another User",
        "email": "anotheruser@example.com",
        "is_active": True
    })
    response = client.get(f"/borrow-records/{another_user_id}")
    print(response.json())
    assert response.status_code == 404


def test_return_book_success():
    response = client.patch(f"/borrow-records/return/{valid_book_id}")
    print(response.json())
    assert response.status_code == 200
    data = response.json()
    assert data["return_date"] == str(date.today())
    assert data["book"]["is_available"] is True


def test_return_book_not_found():
    response = client.patch(f"/borrow-records/return/{invalid_book_id}")
    print(response.json())
    assert response.status_code == 404


def test_return_book_already_returned():
    client.patch(f"/borrow-records/return/{valid_book_id}")
    response = client.patch(f"/borrow-records/return/{valid_book_id}")
    print(response.json())
    assert response.status_code == 400
