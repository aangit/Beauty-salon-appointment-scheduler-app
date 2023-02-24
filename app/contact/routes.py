from fastapi import APIRouter, Depends
from app.contact.controller.contact_controller import ContactController
from app.contact.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer

contact_router = APIRouter(tags=["contact"], prefix="/api/contact")


@contact_router.post("/add-new-contact", response_model=ContactSchema, dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def create_contact(contact: ContactSchemaIn):
    """
    It takes a ContactSchemaIn object, and returns a Contact object
    
    :param contact: ContactSchemaIn
    :type contact: ContactSchemaIn
    :return: The return value is a tuple of (status_code, response_body)
    """
    return ContactController.create_contact(contact.contact_title, contact.user_id, contact.contact_type_id)       


@contact_router.get("/id", response_model=ContactSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_contact_by_id(contact_id: str):
    """
    This function returns a contact object by its id
    
    :param contact_id: str
    :type contact_id: str
    :return: A contact object
    """
    return ContactController.get_contact_by_id(contact_id) 


@contact_router.get("/get-all-contacts", response_model=list[ContactSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_all_contacts():
    """
    It returns all contacts from the database
    :return: A list of all the contacts in the database.
    """
    return ContactController.get_all_contacts()   

@contact_router.delete("/", dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def delete_contact_by_id(contact_id: str):
    """
    Delete a contact by id
    
    :param contact_id: str
    :type contact_id: str
    :return: The return value of the function is the return value of the function that is being called.
    """
    return ContactController.delete_contact_by_id(contact_id) 