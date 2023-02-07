from app.db.database import Base
from sqlalchemy import Column, String
from uuid import uuid4

class UserType(Base):
    __tablename__ = "usertype"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    user_type = Column(String(100))

    def __init__(self, user_type):
        self.user_type = user_type
    