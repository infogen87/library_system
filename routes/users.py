from fastapi import APIRouter
from schemas.users import CreateUser, UpdateUser, users
from services.users import UserCrud

users_router = APIRouter()
 
@users_router.get("/")
def get_all_users():
    return {"all users": {users}}


@users_router.get("/{user_id}")
def get_user(user_id: int):
    UserCrud.get_user_by_id(user_id)
    

@users_router.post("/") 
def create_user(user: CreateUser):
    UserCrud.create_new_user(user)   


@users_router.patch("/{user_id}")
def update_user(user_id: int, user_data: UpdateUser):
    UserCrud.update_user_by_id(user_id, user_data)


@users_router.delete("/{user_id}")
def delete_user(user_id: int):
    UserCrud.delete_user_by_id(user_id)
    