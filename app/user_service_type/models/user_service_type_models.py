from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class UserServiceType(Base):
    __tablename__ = "userservicetype"

    user_id = Column(String(45), ForeignKey("user.id"), primary_key = True, autoincrement = False)
    user = relationship("User", lazy='subquery')

    service_type_id = Column(String(45), ForeignKey("servicetype.id"), primary_key = True, autoincrement = False)
    service_type = relationship("ServiceType", lazy='subquery')   

    def __init__(self, user_id, service_type_id):
        self.user_id = user_id
        self.service_type_id = service_type_id