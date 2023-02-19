from app import user_type
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    email = Column(String(100), unique=True)
    password = Column(String(100))

    user_type_id = Column(String(45), ForeignKey("usertype.id"))
    user_type = relationship("UserType", lazy='subquery')

    def __init__(self, email, password, user_type_id):
        self.email = email
        self.password = password
        self.user_type_id = user_type_id
