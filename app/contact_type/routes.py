from fastapi import APIRouter
from app.contact_type.controller.contact_type_controller import ContactTypeController
from app.contact_type.schemas import *

contact_type_router = APIRouter(tags=["contact-type"], prefix="/api/contact-type")


@contact_type_router.post("/add-new-contact-type", response_model=ContactTypeSchema)
def create_contact_type(contact_type: ContactTypeSchemaIn):
    return ContactTypeController.create_contact_type(contact_type.contact_type) 


@contact_type_router.get("/id", response_model=ContactTypeSchema)
def get_contact_type_by_id(contact_type_id: str):
    return ContactTypeController.get_contact_type_by_id(contact_type_id)    


@contact_type_router.get("/get-all-contact-types", response_model=list[ContactTypeSchema])
def get_all_contact_types():
    return ContactTypeController.get_all_contact_types()

@contact_type_router.delete("/")
def delete_contact_type_by_id(contact_type_id: str):
    return ContactTypeController.delete_contact_type_by_id(contact_type_id)      

@contact_type_router.put("/update", response_model=ContactTypeSchema)
def update_contact_type(contact_type_id, contact_type):
    return ContactTypeController.update_contact_type(contact_type_id, contact_type)
