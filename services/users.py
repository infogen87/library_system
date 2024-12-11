from schemas.users import users, CreateUser, UpdateUser
from fastapi import HTTPException
from typing import Dict

class UserCrud:
    @staticmethod
    def get_user_by_id(id: int):

        user = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        return {"user": {user}}


    @staticmethod
    def create_new_user(user_data: CreateUser):
        user_id = len(users) + 1
        user = {"id": user_id, **user_data.model_dump()}
        users[user_id] = user
        return {"message": "user created successfully!", "new user": {user}}


    @staticmethod
    def update_user_by_id(id: int, user_data: UpdateUser):
        user = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        user.id = user_data.id
        user.name = user_data.name
        user.email = user_data.email
        return {"updated user": {user}, "message": "user updated successfully"}


    @staticmethod
    def delete_user_by_id(id: int):
        user = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        del users[user]
        return {"message": "user deleted successfully"}
