from app.db.database import SessionLocal
from app.user.repository.user_repository import UserRepository
from app.user.exceptions import UserInvalidPassword
import hashlib

class UserServices:

    @staticmethod
    def create_user(email, password: str, user_type_id):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_user(email, hashed_password, user_type_id)
            except Exception as e:
                raise e


    @staticmethod
    def create_super_user(email, password):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()
                return user_repository.create_super_user(email, hashed_password)
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


    @staticmethod
    def login_user(email: str, password: str):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.read_user_by_email(email)
                if hashlib.sha256(bytes(password, "utf-8")).hexdigest() != user.password:
                    raise UserInvalidPassword(message="Invalid password for user", code=401)
                return user
            except Exception as e:
                raise e
