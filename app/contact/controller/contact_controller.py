from sqlalchemy.exc import IntegrityError
from app.contact.service import ContactServices
from fastapi import HTTPException, Response
from app.user.exceptions import UserNotFound
from app.contact_type.exceptions import ContactTypeNotFound
from app.contact.exceptions import ContactNotFound

class ContactController:
    @staticmethod
    def create_contact(contact_title, user_id, contact_type_id):
        try:
            contact = ContactServices.create_contact(contact_title, user_id, contact_type_id) 
            return contact
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ContactTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_contact_by_id(contact_id: str):
        contact = ContactServices.get_contact_by_id(contact_id)
        if contact:
            return contact
        else:
            raise HTTPException(status_code=400, detail=f"Contact with provided id {contact_id} does not exist")

    @staticmethod
    def get_all_contacts():
        contacts = ContactServices.get_all_contacts() 
        return contacts

    @staticmethod
    def delete_contact_by_id(contact_id: str):
        try:
            ContactServices.delete_contact_by_id(contact_id)
            return Response(content=f"Contact with id - {contact_id} is deleted")
        except ContactNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

