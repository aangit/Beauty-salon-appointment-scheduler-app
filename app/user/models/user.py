from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    name = Column(String(100))

    user_type_id = Column(String(45), ForeignKey("usertype.id"))
    user = relationship("UserType", lazy='subquery')

    def __init__(self, name, user_type_id):
        self.name = name
        self.user_type_id = user_type_id
