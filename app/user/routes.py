from fastapi import APIRouter, Depends
from app.user.controller.user_controller import UserController
from app.user.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer
user_router = APIRouter(tags=["user"], prefix="/api/user")


@user_router.post("/add-new-user", response_model=UserSchema)
def create_user(user: UserSchemaIn):
    return UserController.create_user(user.email, user.password, user.user_type_id)  

@user_router.post("/add-new-super-user", response_model=UserSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_super_user(user: UserSchemaIn):
    return UserController.create_super_user(user.email, user.password)

@user_router.post("/login")
def login_user(user: UserSchemaIn):
    return UserController.login_user(user.email, user.password)


@user_router.get("/id", response_model=UserSchema)
def get_user_by_id(user_id: str):
    return UserController.get_user_by_id(user_id)  


@user_router.get("/get-all-users", response_model=list[UserSchema])
def get_all_users():
    return UserController.get_all_users()      

@user_router.delete("/")
def delete_user_by_id(user_id: str):
    return UserController.delete_user_by_id(user_id)    