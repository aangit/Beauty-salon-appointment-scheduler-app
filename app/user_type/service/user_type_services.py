# from app.user_type.repository import user_type_repository
from app.user_type.repository.user_type_repository import UserTypeRepository
from app.db.database import SessionLocal
from app.user_type.exceptions import *

class UserTypeServices:
    @staticmethod
    def create_user_type(user_type):
        try:
            with SessionLocal() as db:
                user_type_repository = UserTypeRepository(db)
                u_type = user_type_repository.read_user_type_by_type(user_type)
                if u_type is None:
                    return user_type_repository.create_user_type(user_type)
                raise UserTypeExistsException(message="Type already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_user_type_by_id(user_type_id: str):
        try:
            with SessionLocal() as db:
                user_type_repository = UserTypeRepository(db)
                return user_type_repository.read_user_type_by_id(user_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_user_types():
        with SessionLocal() as db:
            user_type_repository = UserTypeRepository(db)
            return user_type_repository.read_all_user_types()

    @staticmethod
    def delete_user_type_by_id(user_type_id: str):
        try:
            with SessionLocal() as db:
                user_type_repository = UserTypeRepository(db)
                user_type_repository.delete_user_type_by_id(user_type_id)      
        except Exception as e:
            raise e

    @staticmethod
    def update_user_type(user_type_id: str, user_type: str):
        try:
            with SessionLocal() as db:
                user_type_repository = UserTypeRepository(db)                  
                return user_type_repository.update_employee_type(user_type_id, user_type)        
        except Exception as e:
            raise e