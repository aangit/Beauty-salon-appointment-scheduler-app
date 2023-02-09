from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
# from app.user_type.models import User
from app.user.models import User


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name, user_type_id):
        try:
            user = User(name, user_type_id)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            raise e

    def get_user_by_id(self, user_id: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        return user

    def get_all_users(self):
        users = self.db.query(User).all()
        return users

    def delete_user_by_id(self, user_id:str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            self.db.delete(user)
            self.db.commit()
            return True
        except Exception as e:
            raise e