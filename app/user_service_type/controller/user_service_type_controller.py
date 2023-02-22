from sqlalchemy.exc import IntegrityError
from app.user_service_type.service import UserServiceTypeServices
from fastapi import HTTPException

class UserServiceTypeController:
    @staticmethod
    def create_user_service_type(user_id, service_type_id):
        try:
            user_service_type = UserServiceTypeServices.create_user_service_type(user_id, service_type_id)
            return user_service_type
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User {user_id} with {service_type_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_all_users_service_types():
        users_service_types = UserServiceTypeServices.get_all_users_service_types()   
        return users_service_types

 
