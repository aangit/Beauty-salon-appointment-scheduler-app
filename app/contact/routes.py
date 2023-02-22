from fastapi import APIRouter, Depends
from app.contact.controller.contact_controller import ContactController
from app.contact.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer

contact_router = APIRouter(tags=["contact"], prefix="/api/contact")


@contact_router.post("/add-new-contact", response_model=ContactSchema, dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def create_contact(contact: ContactSchemaIn):
    return ContactController.create_contact(contact.contact_title, contact.user_id, contact.contact_type_id)       


@contact_router.get("/id", response_model=ContactSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_contact_by_id(contact_id: str):
    return ContactController.get_contact_by_id(contact_id) 


@contact_router.get("/get-all-contacts", response_model=list[ContactSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_all_contacts():
    return ContactController.get_all_contacts()   

@contact_router.delete("/", dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def delete_contact_by_id(contact_id: str):
    return ContactController.delete_contact_by_id(contact_id) 