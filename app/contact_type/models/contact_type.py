from app.db.database import Base
from sqlalchemy import Column, String
from uuid import uuid4

class ContactType(Base):
    __tablename__ = "contacttype"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    contact_type = Column(String(100))

    def __init__(self, contact_type):
        self.contact_type = contact_type
    