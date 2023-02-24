from app.db.database import SessionLocal
from app.contact.repository import ContactRepository

class ContactServices:

    @staticmethod
    def create_contact(contact_title, user_id, contact_type_id):
        """
        It creates a contact in the database.
        
        :param contact_title: "John Doe"
        :param user_id: 1
        :param contact_type_id: 1
        :return: The return value is the newly created contact object.
        """
        with SessionLocal() as db:
            try:
                contact_repository = ContactRepository(db)
                return contact_repository.create_contact(contact_title, user_id, contact_type_id)       
            except Exception as e:
                raise e

    @staticmethod
    def get_contact_by_id(contact_id: str):
        """
        It gets a contact by id
        
        :param contact_id: str
        :type contact_id: str
        :return: A Contact object
        """
        with SessionLocal() as db:
            try:
                contact_repository = ContactRepository(db)
                return contact_repository.get_contact_by_id(contact_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_contacts():
        """
        It creates a database session, creates a contact repository, and then calls the
        get_all_contacts() function on the contact repository.
        :return: A list of Contact objects
        """
        with SessionLocal() as db:
            contact_repository = ContactRepository(db)
            return contact_repository.get_all_contacts()   

    @staticmethod
    def delete_contact_by_id(contact_id: str):
        """
        It deletes a contact from the database by its id
        
        :param contact_id: str
        :type contact_id: str
        :return: The return value is the number of rows deleted.
        """
        try:
            with SessionLocal() as db:
                contact_repository = ContactRepository(db)
                return contact_repository.delete_contact_by_id(contact_id)
        except Exception as e:
            raise e


