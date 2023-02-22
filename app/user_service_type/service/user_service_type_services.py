from typing import List
from app.db.database import SessionLocal
from app.service_type.repository import ServiceTypeRepository
from app.user.repository import UserRepository
from app.user_service_type.repository import UserServiceTypeRepository

class UserServiceTypeServices:

    @staticmethod
    def create_user_service_type(user_id, service_type_id):
        with SessionLocal() as db:
            try:
                users_service_types_repository = UserServiceTypeRepository(db)
                return users_service_types_repository.create_user_service_type(user_id, service_type_id)              
            except Exception as e:
                raise e


    @staticmethod
    def get_all_users_service_types():
        with SessionLocal() as db:
            users_service_types_repository = UserServiceTypeRepository(db)
            return users_service_types_repository.get_all_users_service_types()    

