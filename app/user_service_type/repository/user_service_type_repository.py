from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.user_service_type.models import UserServiceType


class UserServiceTypeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_user_service_type(self, user_id, service_type_id):
        try:
            user_service_type = UserServiceType(user_id, service_type_id)
            self.db.add(user_service_type)
            self.db.commit()
            self.db.refresh(user_service_type)
            return user_service_type
        except IntegrityError as e:
            raise e


    def get_all_users_service_types(self):
        users_service_types = self.db.query(UserServiceType).all()
        return users_service_types

