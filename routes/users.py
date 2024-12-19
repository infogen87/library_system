from fastapi import APIRouter, status
from schemas.users import CreateUser, UpdateUser, users
from services.users import UserCrud
from uuid import UUID


users_router = APIRouter()
 
@users_router.get("/", status_code=status.HTTP_200_OK)
def get_all_users():
    return {"all users": list(users.values())}


@users_router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: UUID):
    user = UserCrud.get_user_by_id(user_id)
    return {"user": user}
    

@users_router.post("/", status_code=201) 
def create_user(user: CreateUser):
    UserCrud.create_new_user(user)
    return {"mesage": "new user created successfully", "new user": user}   


@users_router.patch("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: UUID, user_data: UpdateUser):
    user = UserCrud.update_user_by_id(user_id, user_data)
    return {"message": "user updated successfully", "updated user": user} 


@users_router.delete("/{user_id}", status_code=200)
def delete_user(user_id: UUID):
    UserCrud.delete_user_by_id(user_id)
    return {"message": "user deleted successfully"}


@users_router.patch("/{user_id}/deactivate", status_code=status.HTTP_200_OK)
def deactivate_user(user_id: UUID):
    user = UserCrud.deactivate_user_by_id(user_id)
    return {"message": f"user {user.name} has been deactivated"}
    


@users_router.patch("/{user_id}/activate", status_code=status.HTTP_200_OK)
def activate_user(user_id: int):
    user = UserCrud.activate_user_by_id(user_id)
    return {"message": f"user {user.name} has been activated"}           
