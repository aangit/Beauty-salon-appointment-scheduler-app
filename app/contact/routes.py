from fastapi import APIRouter
from app.contact.controller.contact_controller import ContactController
from app.contact.schemas import *

contact_router = APIRouter(tags=["contact"], prefix="/api/contact")


@contact_router.post("/add-new-contact", response_model=ContactSchema)
def create_contact(contact: ContactSchemaIn):
    return ContactController.create_contact(contact.contact_title, contact.user_id, contact.contact_type_id)       


@contact_router.get("/id", response_model=ContactSchema)
def get_contact_by_id(contact_id: str):
    return ContactController.get_contact_by_id(contact_id) 


@contact_router.get("/get-all-contacts", response_model=list[ContactSchema])
def get_all_contacts():
    return ContactController.get_all_contacts()   

@contact_router.delete("/")
def delete_contact_by_id(contact_id: str):
    return ContactController.delete_contact_by_id(contact_id) 