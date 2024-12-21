import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user():
    response = client.post(
        "/users/",
        json={"name": "Test User", "email": "testuser@example.com"}
    )
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["name"] == "Test User"
    assert data["email"] == "testuser@example.com"


def test_get_user_by_id():
    create_response = client.post(
        "/users/",
        json={"name": "Test User", "email": "testuser@example.com"}
    )
    user_id = create_response.json()["id"]

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
    assert data["name"] == "Test User"
    assert data["email"] == "testuser@example.com"


def test_get_all_users():
    client.post("/users/", json={"name": "User1", "email": "user1@example.com"})
    client.post("/users/", json={"name": "User2", "email": "user2@example.com"})

    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2


def test_update_user():
    create_response = client.post(
        "/users/",
        json={"name": "Original User", "email": "original@example.com"}
    )
    user_id = create_response.json()["id"]

    update_response = client.put(
        f"/users/{user_id}",
        json={"name": "Updated User", "email": "updated@example.com"}
    )
    assert update_response.status_code == 200
    data = update_response.json()
    assert data["name"] == "Updated User"
    assert data["email"] == "updated@example.com"

    fetch_response = client.get(f"/users/{user_id}")
    assert fetch_response.status_code == 200
    fetch_data = fetch_response.json()
    assert fetch_data["name"] == "Updated User"
    assert fetch_data["email"] == "updated@example.com"


def test_delete_user():
    create_response = client.post(
        "/users/",
        json={"name": "User to Delete", "email": "delete@example.com"}
    )
    user_id = create_response.json()["id"]

    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "User deleted successfully"}

    fetch_response = client.get(f"/users/{user_id}")
    assert fetch_response.status_code == 404
    assert fetch_response.json() == {"detail": "User not found"}
