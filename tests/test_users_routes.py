from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# fake_users = {[
#     {
#       "name": "aew",
#       "email": "awr@gmail.com",
#       "is_active": True,
#       "id": 1
#     },
#     {
#       "name": "aew",
#       "email": "awr@gmail.com",
#       "is_active": True,
#       "id": 2
#     },
#     {
#       "name": "aew",
#       "email": "awr@gmail.com",
#       "is_active": True,
#       "id": 3
#     },
#     {
#       "name": "aew",
#       "email": "awr@gmail.com",
#       "is_active": True,
#       "id": 4
#     }
#   ]}

def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200


def test_get_user_id():
    response = client.get("/users/1",params={"name": "aew",
      "email": "awr@gmail.com"})
    assert response.status_code == 200
    assert response.json == {
      "name": "aew",
      "email": "awr@gmail.com",
      "is_active": True,
      "id": 1
    }



def test_create_user():
    
    response = client.post("/", json={
  "mesage": "new user created successfully",
  "new user": {
    "name": "aew",
    "email": "awr@gmail.com",
    "is_active": True
  }
})
    assert response.json == {
  "mesage": "new user created successfully",
  "new user": {
    "name": "aew",
    "email": "awr@gmail.com",
    "is_active": True
  }
}
# def test_update_user_by_id():
#     response = client.    


# def test_delete_user():
#     response = client.delete("/")


# def test_activate_user():
#     response = client.patch


# def test_deactivate_user():
#     response = client.patch
