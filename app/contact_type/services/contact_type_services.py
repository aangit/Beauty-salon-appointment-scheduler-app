from app.contact_type.repository import ContactTypeRepository
from app.db.database import SessionLocal
from app.contact_type.exceptions import ContactTypeExists

class ContactTypeServices:
    @staticmethod
    def create_contact_type(contact_type):
        """
        If the contact type exists in the database, raise an exception. If it doesn't, create it
        
        :param contact_type: This is the type of contact, e.g. email, phone, etc
        :return: The return value is a ContactType object.
        """
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)
                c_type = contact_type_repository.read_contact_type_by_type(contact_type)
                if c_type is None:
                    return contact_type_repository.create_contact_type(contact_type)      
                raise ContactTypeExists(message="Contact type already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_contact_type_by_id(contact_type_id: str):
        """
        It gets a contact type by id
        
        :param contact_type_id: str
        :type contact_type_id: str
        :return: A ContactType object
        """
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)
                return contact_type_repository.read_contact_type_by_id(contact_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_contact_types():
        """
        It returns all the contact types from the database.
        :return: A list of ContactType objects
        """
        with SessionLocal() as db:
            contact_type_repository = ContactTypeRepository(db)
            return contact_type_repository.read_all_contact_types()

    @staticmethod
    def delete_contact_type_by_id(contact_type_id: str):
        """
        It deletes a contact type by id
        
        :param contact_type_id: str
        :type contact_type_id: str
        """
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)
                contact_type_repository.delete_contact_type_by_id(contact_type_id)     
        except Exception as e:
            raise e

    @staticmethod
    def update_contact_type(contact_type_id: str, contact_type: str):
        """
        It updates the contact type in the database
        
        :param contact_type_id: str = "1"
        :type contact_type_id: str
        :param contact_type: str = Body(..., embed=True)
        :type contact_type: str
        :return: The return value is a tuple of the form (rowcount, lastrowid)
        """
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)                  
                return contact_type_repository.update_contact_type(contact_type_id, contact_type)          
        except Exception as e:
            raise e
