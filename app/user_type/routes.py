from fastapi import APIRouter
from app.user_type.controller.user_type_controller import UserTypeController

from app.user_type.schemas import *

user_type_router = APIRouter(tags=["user-type"], prefix="/api/user-type")


@user_type_router.post("/add-new-user-type", response_model=UserTypeSchema)
def create_user_type(user_type: UserTypeSchemaIn):
    return UserTypeController.create_user_type(user_type.user_type)


@user_type_router.get("/id", response_model=UserTypeSchema)
def get_user_type_by_id(user_type_id: str):
    return UserTypeController.get_user_type_by_id(user_type_id)          


@user_type_router.get("/get-all-user-types", response_model=list[UserTypeSchema])
def get_all_user_types():
    return UserTypeController.get_all_user_types()

@user_type_router.delete("/")
def delete_user_type_by_id(user_type_id: str):
    return UserTypeController.delete_user_type_by_id(user_type_id)        

@user_type_router.put("/update", response_model=UserTypeSchema)
def update_user_type(user_type_id, user_type):
    return UserTypeController.update_user_type(user_type_id, user_type)
