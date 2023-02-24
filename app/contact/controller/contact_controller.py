from app.contact.service import ContactServices
from fastapi import HTTPException, Response
from app.user.exceptions import UserNotFound
from app.contact_type.exceptions import ContactTypeNotFound
from app.contact.exceptions import ContactNotFound

class ContactController:
    @staticmethod
    def create_contact(contact_title, user_id, contact_type_id):
        """
        It creates a contact
        
        :param contact_title: The title of the contact
        :param user_id: The id of the user who created the contact
        :param contact_type_id: 1
        :return: The return value is a Contact object.
        """
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
        """
        If the contact exists, return it, otherwise raise an exception
        
        :param contact_id: str
        :type contact_id: str
        :return: The contact object
        """
        contact = ContactServices.get_contact_by_id(contact_id)
        if contact:
            return contact
        else:
            raise HTTPException(status_code=400, detail=f"Contact with provided id {contact_id} does not exist")

    @staticmethod
    def get_all_contacts():
        """
        It returns a list of all contacts from the database
        :return: A list of contacts
        """
        contacts = ContactServices.get_all_contacts() 
        return contacts

    @staticmethod
    def delete_contact_by_id(contact_id: str):
        """
        It deletes a contact by id
        
        :param contact_id: str
        :type contact_id: str
        :return: Response(content=f"Contact with id - {contact_id} is deleted")
        """
        try:
            ContactServices.delete_contact_by_id(contact_id)
            return Response(content=f"Contact with id - {contact_id} is deleted")
        except ContactNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

