from fastapi import APIRouter, Depends
from app.user_type.controller.user_type_controller import UserTypeController
from app.user.controller.user_authenification_controller import JWTBearer
from app.user_type.schemas import *

user_type_router = APIRouter(tags=["user-type"], prefix="/api/user-type")


@user_type_router.post("/add-new-user-type", response_model=UserTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_user_type(user_type: UserTypeSchemaIn):
    """
    It takes a UserTypeSchemaIn object, and returns a UserType object
    
    :param user_type: UserTypeSchemaIn
    :type user_type: UserTypeSchemaIn
    :return: The return value is a UserTypeSchemaOut object.
    """
    return UserTypeController.create_user_type(user_type.user_type)


@user_type_router.get("/id", response_model=UserTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def get_user_type_by_id(user_type_id: str):
    """
    This function returns a user type object by its id
    
    :param user_type_id: str
    :type user_type_id: str
    :return: A UserType object
    """
    return UserTypeController.get_user_type_by_id(user_type_id)          


@user_type_router.get("/get-all-user-types", response_model=list[UserTypeSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_user_types():
    """
    This function returns all user types from the database
    :return: A list of UserType objects
    """
    return UserTypeController.get_all_user_types()

@user_type_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_user_type_by_id(user_type_id: str):
    """
    Delete a user type by id
    
    :param user_type_id: str
    :type user_type_id: str
    :return: The return value of the function is the return value of the function that is being called.
    """
    return UserTypeController.delete_user_type_by_id(user_type_id)        

@user_type_router.put("/update", response_model=UserTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def update_user_type(user_type_id, user_type):
    """
    It updates the user type in the database
    
    :param user_type_id: The id of the user type to update
    :param user_type: {
    :return: The return value of the function update_user_type()
    """
    return UserTypeController.update_user_type(user_type_id, user_type)
