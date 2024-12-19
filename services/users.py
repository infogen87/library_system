from schemas.users import users, CreateUser, UpdateUser, User
from fastapi import HTTPException
from uuid import UUID, uuid4


class UserCrud:
    @staticmethod
    def get_user_by_id(id: UUID):
        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        return user


    @staticmethod
    def create_new_user(user_data: CreateUser):
        user_id = uuid4()
        user = User(id=user_id, **user_data.model_dump())
        users[user_id] = user
        return user
        
    

    @staticmethod
    def update_user_by_id(id: UUID, user_data: UpdateUser):
        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        if user.is_active == False:
            raise HTTPException(status_code=403, detail="user is not active!")
        for k, v in user_data.model_dump().items():
            setattr(user, k, v)
        return user

      

    @staticmethod
    def delete_user_by_id(user_id: UUID):
        if user_id not in users:
            raise HTTPException(status_code=404, detail="user not found!")
        del users[user_id]
        return
        
    

    @staticmethod
    def deactivate_user_by_id(id: UUID):
        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        if user.is_active == False:
            raise HTTPException(status_code=400, detail="user is already deactivated!")
        user.is_active = False
        return user


    @staticmethod
    def activate_user_by_id(id: UUID):
        user: User = users.get(id)
        if not user:
            raise HTTPException(status_code=404, detail="user not found!")
        if user.is_active == True:
            raise HTTPException(status_code=400, detail="user is already active")
        user.is_active = True
        return user