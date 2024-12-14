from schemas.users import users, CreateUser, UpdateUser, User
from fastapi import HTTPException


class UserCrud:
    @staticmethod
    def get_user_by_id(id: int):

        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        return {"user": user}


    @staticmethod
    def create_new_user(user_data: CreateUser):
        user_id = len(users) + 1
        user = User(id=user_id, **user_data.model_dump())
        users[user_id] = user
        return {"mesage": "new user created successfully", "new user": user}
        
    

    @staticmethod
    def update_user_by_id(id: int, user_data: UpdateUser):
        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        if user.is_active == False:
        # if user[is_active] == False:
            raise HTTPException(status_code=403, detail="user is not active!")
        for k, v in user_data.model_dump().items():
            setattr(user, k, v)
        return {"message": "user updated successfully", "updated user": user}    

    

    @staticmethod
    def delete_user_by_id(id: int):
        user = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        del users[user]
        return {"message": "user deleted successfully"}
    

    @staticmethod
    def deactivate_user_by_id(id: int):
        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        if user.is_active == False:
            raise HTTPException(status_code=400, detail="user is already deactivated!")
        user.is_active = False
        return {"message": f"user {user.name} has been deactivated"}


    @staticmethod
    def activate_user_by_id(id: int):
        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        if user.is_active == True:
            raise HTTPException(status_code=400, detail="user is already active")
        user.is_active = True
        return {"message": f"user {user.name} has been activated"}    