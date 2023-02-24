from fastapi import APIRouter, Depends
from app.contact_type.controller.contact_type_controller import ContactTypeController
from app.contact_type.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer

contact_type_router = APIRouter(tags=["contact-type"], prefix="/api/contact-type")


@contact_type_router.post("/add-new-contact-type", response_model=ContactTypeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def create_contact_type(contact_type: ContactTypeSchemaIn):
    """
    Create a contact type
    
    :param contact_type: ContactTypeSchemaIn
    :type contact_type: ContactTypeSchemaIn
    :return: The return value is a ContactTypeSchemaOut object.
    """
    return ContactTypeController.create_contact_type(contact_type.contact_type) 


@contact_type_router.get("/id", response_model=ContactTypeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_contact_type_by_id(contact_type_id: str):
    """
    Get a contact type by its id
    
    :param contact_type_id: str
    :type contact_type_id: str
    :return: A ContactType object
    """
    return ContactTypeController.get_contact_type_by_id(contact_type_id)    


@contact_type_router.get("/get-all-contact-types", response_model=list[ContactTypeSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_all_contact_types():
    """
    This function returns a list of all contact types
    :return: A list of ContactType objects
    """
    return ContactTypeController.get_all_contact_types()

@contact_type_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_contact_type_by_id(contact_type_id: str):
    """
    Delete a contact type by id
    
    :param contact_type_id: str
    :type contact_type_id: str
    :return: The return value of the function is the return value of the function that is being called.
    """
    return ContactTypeController.delete_contact_type_by_id(contact_type_id)      

@contact_type_router.put("/update", response_model=ContactTypeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def update_contact_type(contact_type_id, contact_type):
    """
    Update a contact type by id
    
    :param contact_type_id: The id of the contact type to update
    :param contact_type: 
    :return: The return value of the function update_contact_type()
    """
    return ContactTypeController.update_contact_type(contact_type_id, contact_type)
