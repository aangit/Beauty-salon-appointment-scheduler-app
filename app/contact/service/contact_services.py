from app.db.database import SessionLocal
from app.contact.repository.contact_repository import ContactRepository

class ContactServices:

    @staticmethod
    def create_contact(contact_title, user_id, contact_type_id):
        with SessionLocal() as db:
            try:
                contact_repository = ContactRepository(db)
                return contact_repository.create_contact(contact_title, user_id, contact_type_id)       
            except Exception as e:
                raise e

    @staticmethod
    def get_contact_by_id(contact_id: str):
        with SessionLocal() as db:
            try:
                contact_repository = ContactRepository(db)
                return contact_repository.get_contact_by_id(contact_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_contacts():
        with SessionLocal() as db:
            contact_repository = ContactRepository(db)
            return contact_repository.get_all_contacts()   

    @staticmethod
    def delete_contact_by_id(contact_id: str):
        try:
            with SessionLocal() as db:
                contact_repository = ContactRepository(db)
                return contact_repository.delete_contact_by_id(contact_id)
        except Exception as e:
            raise e


