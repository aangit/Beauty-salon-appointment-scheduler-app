from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.contact_type.exceptions import ContactTypeNotFound
from app.contact_type.models import ContactType


class ContactTypeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_contact_type(self, contact_type):
        try:
            contact_type = ContactType(contact_type)
            self.db.add(contact_type)
            self.db.commit()
            self.db.refresh(contact_type)
            return contact_type
        except IntegrityError as e:
            raise e

    def read_contact_type_by_id(self, contact_type_id: str):
        contact_type= self.db.query(ContactType).filter(ContactType.id == contact_type_id).first()
        if contact_type is None:
            raise ContactTypeNotFound(f"Contact type with provided ID: {contact_type_id} not found.", 400)
        return contact_type

    def read_contact_type_by_type(self, contact_type: str):
        c_type = self.db.query(ContactType).filter(ContactType.contact_type == contact_type).first()
        return c_type

    def read_all_contact_types(self):
        contact_types = self.db.query(ContactType).all()
        return contact_types

    def delete_contact_type_by_id(self, contact_type_id: str):
        try:
            contact_type = self.db.query(ContactType).filter(ContactType.id == contact_type_id).first()
            if contact_type is None:
                raise  ContactTypeNotFound(f"Contact type with provided ID: {contact_type_id} not found", 400)
            self.db.delete(contact_type)
            self.db.commit()
            return True
        except Exception as e:
            raise e

    def update_contact_type(self, contact_type_id: str, contact_type: str):
        try:
            c_type = self.db.query(ContactType).filter(ContactType.id == contact_type_id).first()
            if c_type is None:
                raise ContactTypeNotFound(f"Contact type with provided ID: {contact_type_id} not found", 400) 
            c_type.contact_type = contact_type
            self.db.add(c_type)
            self.db.commit()
            self.db.refresh(c_type)
            return c_type
        except Exception as e:
            raise e