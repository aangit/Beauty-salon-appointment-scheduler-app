from sqlalchemy.exc import IntegrityError
from app.user.service import UserServices
from fastapi import HTTPException, Response
# from app.users.exceptions import UserInvalidePassword

class UserController:
    @staticmethod
    def create_user(name, user_type_id):
        try:
            user = UserServices.create_user(name, user_type_id)
            return user
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User with provided id - {user_type_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_by_id(user_id: str):
        user = UserServices.get_user_by_id(user_id)
        if user:
            return user
        else:
            raise HTTPException(status_code=400, detail=f"user with provided id {user_id} does not exist")

    @staticmethod
    def get_all_users():
        users = UserServices.get_all_users()
        return users

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            UserServices.delete_user_by_id(user_id)
            return Response(content=f"User with id - {user_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
