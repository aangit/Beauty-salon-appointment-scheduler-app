from fastapi import APIRouter, Depends
from app.service_type.controller import ServiceTypeController

from app.service_type.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer
from app.user.schemas import UserSchema

service_type_router = APIRouter(tags=["service-type"], prefix="/api/service-type")


@service_type_router.post("/add-new-service-type", response_model=ServiceTypeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def create_service_type(service_type: ServiceTypeSchemaIn):
    """
    It takes a ServiceTypeSchemaIn object, and returns a ServiceType object
    
    :param service_type: ServiceTypeSchemaIn
    :type service_type: ServiceTypeSchemaIn
    :return: A ServiceType object
    """
    return ServiceTypeController.create_service_type(service_type.service_name, service_type.approximate_duration, service_type.price, service_type.available_at)


@service_type_router.get("/id", response_model=ServiceTypeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def read_service_type_by_id(service_type_id: str):
    """
    Reads a service type by its id
    
    :param service_type_id: str
    :type service_type_id: str
    :return: A ServiceType object
    """
    return ServiceTypeController.read_service_type_by_id(service_type_id)           

@service_type_router.get("/read-service-type-by-name-partially", response_model=list[ServiceTypeSchema], dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def read_service_type_by_name_partially(service_name: str):
    """
    Reads a service type by name partially (based on a keyword by user's input)
    
    :param service_name: str
    :type service_name: str
    :return: A list of ServiceType objects
    """
    return ServiceTypeController.read_service_type_by_name_partially(service_name)           

@service_type_router.get("/get-all-service-types", response_model=list[ServiceTypeSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def read_all_service_types():
    """
    Read all service types from the database
    :return: A list of ServiceType objects
    """
    return ServiceTypeController.read_all_service_types()

@service_type_router.get("/get-all-users-for-service-type", response_model= list[UserSchema], dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def user_has_service_type(service_type_id: str):
    """
    Returns true if the user has the service type with the given id
    
    :param service_type_id: The id of the service type you want to check if the user has
    :type service_type_id: str
    :return: A boolean value
    """
    return ServiceTypeController.user_has_service_type(service_type_id)

@service_type_router.get("/get-all-users-for-service-type-by-service-type-name", response_model= list[UserSchema], dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def read_users_per_service_type_name(service_name: str):
    """
    Reads all users per service type name
    
    :param service_name: str
    :type service_name: str
    :return: A list of users
    """
    return ServiceTypeController.read_users_per_service_type_name(service_name)
        
          

@service_type_router.delete("/", dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def delete_service_type_by_id(service_type_id: str):
    """
    Delete a service type by id
    
    :param service_type_id: str
    :type service_type_id: str
    :return: The return value of the function is the return value of the function that is being called.
    """
    return ServiceTypeController.delete_service_type_by_id(service_type_id)     


@service_type_router.patch("/update-service-type", response_model = ServiceTypeSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def update_service_type_by_id(service_type_id: str, service_type: UpdateServiceTypeSchemaIn):
    """
    Update a service type by id
    
    :param service_type_id: str
    :type service_type_id: str
    :param service_type: UpdateServiceTypeSchemaIn
    :type service_type: UpdateServiceTypeSchemaIn
    :return: The return value is a ServiceType object.
    """
    return ServiceTypeController.update_service_type_by_id(service_type_id, service_type)


