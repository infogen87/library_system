from fastapi import APIRouter, status, HTTPException
from schemas.users import CreateUser, UpdateUser, users
from services.users import UserCrud


users_router = APIRouter()
 
@users_router.get("/", status_code=200)
def get_all_users():
    return {"all users": list(users.values())}


@users_router.get("/{user_id}", status_code=200)
def get_user(user_id: int):
    UserCrud.get_user_by_id(user_id)
    

@users_router.post("/",status_code=status) 
def create_user(user: CreateUser):
    UserCrud.create_new_user(user)   


@users_router.patch("/{user_id}", status_code=200)
def update_user(user_id: int, user_data: UpdateUser):
    UserCrud.update_user_by_id(user_id, user_data)


@users_router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    UserCrud.delete_user_by_id(user_id)


@users_router.patch("/{user_id}/deactivate", status_code=200)
def deactivate_user(user_id: int):
    UserCrud.deactivate_user_by_id(user_id)


@users_router.patch("/{user_id}/activate", status_code=200)
def activate_user(user_id: int):
    UserCrud.activate_user_by_id(user_id)       
    