from app.contact_type.services.contact_type_services import ContactTypeServices
from app.contact_type.exceptions import ContactTypeExists, ContactTypeNotFound
from fastapi import HTTPException, Response


class ContactTypeController:

    @staticmethod
    def create_contact_type(contact_type):
        """
        It creates a contact type
        
        :param contact_type
        :return: The return value is a ContactType object.
        """
        try:
            c_type = ContactTypeServices.create_contact_type(contact_type)      
            return c_type

        except ContactTypeExists as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_contact_type_by_id(contact_type_id: str):
        """
        It gets a contact type by id
        
        :param contact_type_id: str
        :type contact_type_id: str
        :return: A ContactType object
        """
        try:
            contact_type = ContactTypeServices.get_contact_type_by_id(contact_type_id) 
            if contact_type:
                return contact_type
        except ContactTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_contact_type_by_type_name(contact_type_name: str):
        """
        It gets a contact type by name, and if it doesn't find it, it raises an exception
        
        :param contact_type_name: str
        :type contact_type_name: str
        :return: A ContactType object
        """
        try:
            contact_type = ContactTypeServices.get_contact_type_by_id(contact_type_name)
            if contact_type:
                return contact_type
        except ContactTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_contact_types():
        """
        It returns a list of contact types
        :return: A list of ContactType objects
        """
        contact_types = ContactTypeServices.get_all_contact_types()
        return contact_types
    
    
    @staticmethod
    def delete_contact_type_by_id(contact_type_id: str):
        """
        It deletes a contact type by id
        
        :param contact_type_id: str
        :type contact_type_id: str
        :return: Response(content=f"Contact type with id - {contact_type_id} is deleted")
        """
        try:
            ContactTypeServices.delete_contact_type_by_id(contact_type_id)     
            return Response(content=f"Contact type with id - {contact_type_id} is deleted")
        except ContactTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def update_contact_type(contact_type_id: str, contact_type: str):
        """
        It updates a contact type in the database
        
        :param contact_type_id: str
        :type contact_type_id: str
        :param contact_type: str
        :type contact_type: str
        :return: The return value is a ContactType object.
        """
        try:
            c_type = ContactTypeServices.update_contact_type(contact_type_id, contact_type)     
            return c_type
        except ContactTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))