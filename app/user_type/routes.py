from fastapi import APIRouter, Depends
from app.user_type.controller.user_type_controller import UserTypeController
from app.user.controller.user_authenification_controller import JWTBearer
from app.user_type.schemas import *

user_type_router = APIRouter(tags=["user-type"], prefix="/api/user-type")


@user_type_router.post("/add-new-user-type", response_model=UserTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_user_type(user_type: UserTypeSchemaIn):
    return UserTypeController.create_user_type(user_type.user_type)


@user_type_router.get("/id", response_model=UserTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_user_type_by_id(user_type_id: str):
    return UserTypeController.get_user_type_by_id(user_type_id)          


@user_type_router.get("/get-all-user-types", response_model=list[UserTypeSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_user_types():
    return UserTypeController.get_all_user_types()

@user_type_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_type_by_id(user_type_id: str):
    return UserTypeController.delete_user_type_by_id(user_type_id)        

@user_type_router.put("/update", response_model=UserTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_user_type(user_type_id, user_type):
    return UserTypeController.update_user_type(user_type_id, user_type)
