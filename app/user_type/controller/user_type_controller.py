from app.user_type.service.user_type_services import UserTypeServices
from app.user_type.exceptions import *
from fastapi import HTTPException, Response


class UserTypeController:

    @staticmethod
    def create_user_type(user_type):
        try:
            u_type = UserTypeServices.create_user_type(user_type) 
            return u_type

        except UserTypeExistsException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_type_by_id(user_type_id: str):
        try:
            user_type = UserTypeServices.get_user_type_by_id(user_type_id)
            if user_type:
                return user_type
        except UserTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_user_type_by_type_name(user_type_name: str):
        try:
            user_type = UserTypeServices.get_user_type_by_id(user_type_name)
            if user_type:
                return user_type
        except UserTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_user_types():
        user_types = UserTypeServices.get_all_user_types()
        return user_types
    
    
    @staticmethod
    def delete_user_type_by_id(user_type_id: str):
        try:
            UserTypeServices.delete_user_type_by_id(user_type_id)        
            return Response(content=f"User type with id - {user_type_id} is deleted")
        except UserTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_user_type(user_type_id: str, user_type: str):
        try:
            u_type = UserTypeServices.update_user_type(user_type_id, user_type)        
            return u_type
        except UserTypeNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
