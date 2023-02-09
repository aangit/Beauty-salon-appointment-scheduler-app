from app.contact_type.repository import ContactTypeRepository
from app.db.database import SessionLocal
from app.contact_type.exceptions import *

class ContactTypeServices:
    @staticmethod
    def create_contact_type(contact_type):
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)
                c_type = contact_type_repository.read_contact_type_by_type(contact_type)
                if c_type is None:
                    return contact_type_repository.create_contact_type(contact_type)      
                raise ContactTypeExistsException(message="Contact type already exists in database.", code=400)
        except Exception as e:
            raise e

    @staticmethod
    def get_contact_type_by_id(contact_type_id: str):
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)
                return contact_type_repository.read_contact_type_by_id(contact_type_id)
        except Exception as e:
            raise e

    @staticmethod
    def get_all_contact_types():
        with SessionLocal() as db:
            contact_type_repository = ContactTypeRepository(db)
            return contact_type_repository.read_all_contact_types()

    @staticmethod
    def delete_contact_type_by_id(contact_type_id: str):
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)
                contact_type_repository.delete_contact_type_by_id(contact_type_id)     
        except Exception as e:
            raise e

    @staticmethod
    def update_contact_type(contact_type_id: str, contact_type: str):
        try:
            with SessionLocal() as db:
                contact_type_repository = ContactTypeRepository(db)                  
                return contact_type_repository.update_contact_type(contact_type_id, contact_type)          
        except Exception as e:
            raise e
