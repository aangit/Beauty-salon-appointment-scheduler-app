from fastapi import APIRouter, Depends
from app.user.controller.user_authenification_controller import JWTBearer
from app.user_service_type.controller import UserServiceTypeController
from app.user_service_type.schemas import *

user_service_type_router = APIRouter(tags=["user-service-type"], prefix="/api/user-service-type")


@user_service_type_router.post("/add-new-user-service-type", response_model=UserServiceTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_user_service_type(user_service_type: UserServiceTypeSchemaIn):
    return UserServiceTypeController.create_user_service_type(user_service_type.user_id, user_service_type.service_type_id)       


@user_service_type_router.get("/get-all-user-service-types", response_model=list[UserServiceTypeSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_users_service_types():
    return UserServiceTypeController.get_all_users_service_types()

