from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from uuid import uuid4
from sqlalchemy.orm import relationship


class Contact(Base):
    __tablename__ = "contact"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    contact_title = Column(String(100))

    user_id = Column(String(45), ForeignKey("user.id"))
    user = relationship("User", lazy='subquery')

    contact_type_id = Column(String(50), ForeignKey("contacttype.id"))
    contact_type = relationship("ContactType", lazy = 'subquery')

    def __init__(self, contact_title, user_id, contact_type_id ):
        self.contact_title = contact_title
        self.user_id = user_id
        self.contact_type_id = contact_type_id