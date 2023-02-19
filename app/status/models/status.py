from app.db.database import Base
from sqlalchemy import Column, String
from uuid import uuid4

class Status(Base):
    __tablename__ = "status"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    status = Column(String(100))

    def __init__(self, status):
        self.status = status
    