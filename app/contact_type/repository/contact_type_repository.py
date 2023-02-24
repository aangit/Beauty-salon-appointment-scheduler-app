from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.contact_type.exceptions import ContactTypeNotFound
from app.contact_type.models import ContactType


class ContactTypeRepository:

    def __init__(self, db: Session):
        """
        This function is used to initialize the database session
        
        :param db: Session = Depends(get_db)
        :type db: Session
        """
        self.db = db

    def create_contact_type(self, contact_type):
        """
        It creates a new contact type and adds it to the database.
        
        :param contact_type: 'email'
        :return: The contact_type object
        """
        try:
            contact_type = ContactType(contact_type)
            self.db.add(contact_type)
            self.db.commit()
            self.db.refresh(contact_type)
            return contact_type
        except IntegrityError as e:
            raise e

    def read_contact_type_by_id(self, contact_type_id: str):
        """
        It returns a contact type object from the database if it exists, otherwise it raises an
        exception
        
        :param contact_type_id: str
        :type contact_type_id: str
        :return: The contact_type object
        """
        contact_type= self.db.query(ContactType).filter(ContactType.id == contact_type_id).first()
        if contact_type is None:
            raise ContactTypeNotFound(f"Contact type with provided ID: {contact_type_id} not found.", 400)
        return contact_type

    def read_contact_type_by_type(self, contact_type: str):
        """
        It returns the first contact type that matches the contact type passed in
        
        :param contact_type: str
        :type contact_type: str
        :return: A ContactType object
        """
        c_type = self.db.query(ContactType).filter(ContactType.contact_type == contact_type).first()
        return c_type

    def read_all_contact_types(self):
        """
        It returns all the contact types from the database
        :return: A list of ContactType objects.
        """
        contact_types = self.db.query(ContactType).all()
        return contact_types

    def delete_contact_type_by_id(self, contact_type_id: str):
        """
        It deletes a contact type from the database if it exists
        
        :param contact_type_id: str
        :type contact_type_id: str
        :return: True
        """
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
        """
        It updates the contact type with the provided contact type id and contact type
        
        :param contact_type_id: str
        :type contact_type_id: str
        :param contact_type: str
        :type contact_type: str
        :return: The updated contact type
        """
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