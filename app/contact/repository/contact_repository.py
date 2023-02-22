from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.contact.models import Contact
from app.user.models import User
from app.user.exceptions import UserNotFound
from app.contact_type.models import ContactType
from app.contact_type.exceptions import ContactTypeNotFound
from app.contact.exceptions import ContactNotFound
class ContactRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_contact(self, contact_title, user_id, contact_type_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise UserNotFound(message="There is no such user", code=404)
        
        contact_type = self.db.query(ContactType).filter(ContactType.id == contact_type_id).first()
        if not contact_type:
            raise ContactTypeNotFound(message="There is no such contact type", code=404)
        
        try:
            contact = Contact(contact_title, user_id, contact_type_id)
            self.db.add(contact)
            self.db.commit()
            self.db.refresh(contact)
            return contact
        except IntegrityError as e:
            raise e

    def get_contact_by_id(self, contact_id: str):
        contact = self.db.query(Contact).filter(Contact.id == contact_id).first()
        return contact

    def get_all_contacts(self):
        contacts = self.db.query(Contact).all()
        return contacts

    def delete_contact_by_id(self, contact_id:str):
        try:
            contact = self.db.query(Contact).filter(Contact.id == contact_id).first()
            if not contact:
                raise ContactNotFound(message="There is no such contact", code=404)
            self.db.delete(contact)
            self.db.commit()
            return True
        except Exception as e:
            raise e


