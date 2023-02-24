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
        """
        This function is used to initialize the database session
        
        :param db: Session - the database session
        :type db: Session
        """
        self.db = db

    def create_contact(self, contact_title, user_id, contact_type_id):
        """
        It creates a contact for a user with a given contact type
        
        :param contact_title: The title of the contact
        :param user_id: The id of the user who created the contact
        :param contact_type_id: 1
        :return: The contact object
        """
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
        """
        It returns a contact object from the database, given a contact id
        
        :param contact_id: str
        :type contact_id: str
        :return: A contact object
        """
        contact = self.db.query(Contact).filter(Contact.id == contact_id).first()
        return contact

    def get_all_contacts(self):
        contacts = self.db.query(Contact).all()
        return contacts

    def delete_contact_by_id(self, contact_id:str):
        """
        It deletes a contact from the database by its id
        
        :param contact_id: The id of the contact to be deleted
        :type contact_id: str
        :return: True
        """
        try:
            contact = self.db.query(Contact).filter(Contact.id == contact_id).first()
            if not contact:
                raise ContactNotFound(message="There is no such contact", code=404)
            self.db.delete(contact)
            self.db.commit()
            return True
        except Exception as e:
            raise e


