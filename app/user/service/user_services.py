from app.db.database import SessionLocal
from app.user.repository.user_repository import UserRepository

class UserServices:

    @staticmethod
    def create_user(name, user_type_id):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.create_user(name, user_type_id)          
            except Exception as e:
                raise e

    @staticmethod
    def get_user_by_id(user_id: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                return user_repository.get_user_by_id(user_id=user_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_users():
        with SessionLocal() as db:
            user_repository = UserRepository(db)
            return user_repository.get_all_users()

    @staticmethod
    def delete_user_by_id(user_id: str):
        try:
            with SessionLocal() as db:
                user_repository = UserRepository(db)
                return user_repository.delete_user_by_id(user_id)
        except Exception as e:
            raise e
