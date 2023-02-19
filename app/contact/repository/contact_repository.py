from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.contact.models import Contact

class ContactRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_contact(self, contact_title, user_id, contact_type_id):
        try:
            contact = Contact(contact_title, user_id, contact_type_id )
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
            self.db.delete(contact)
            self.db.commit()
            return True
        except Exception as e:
            raise e