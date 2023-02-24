from sqlalchemy.exc import IntegrityError
from app.user_service_type.service import UserServiceTypeServices
from fastapi import HTTPException

class UserServiceTypeController:
    @staticmethod
    def create_user_service_type(user_id, service_type_id):
        """
        It creates a user_service_type object and returns it
        
        :param user_id
        :param service_type_id
        :return: The return value is a UserServiceType object.
        """
        try:
            user_service_type = UserServiceTypeServices.create_user_service_type(user_id, service_type_id)
            return user_service_type
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"User {user_id} with {service_type_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_all_users_service_types():
        """
        It returns a list of dictionaries, each dictionary containing a user's id, name, and service
        type id.
        :return: A list of dictionaries.
        """
        users_service_types = UserServiceTypeServices.get_all_users_service_types()   
        return users_service_types

 
