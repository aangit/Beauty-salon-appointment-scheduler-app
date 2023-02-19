from fastapi import APIRouter
from app.service_type.controller import ServiceTypeController

from app.service_type.schemas import *

service_type_router = APIRouter(tags=["service-type"], prefix="/api/service-type")


@service_type_router.post("/add-new-service-type", response_model=ServiceTypeSchema)
def create_service_type(service_type: ServiceTypeSchemaIn):
    return ServiceTypeController.create_service_type(service_type.service_name, service_type.approximate_duration, service_type.price, service_type.available_at)


@service_type_router.get("/id", response_model=ServiceTypeSchema)
def read_service_type_by_id(service_type_id: str):
    return ServiceTypeController.read_service_type_by_id(service_type_id)           


@service_type_router.get("/get-all-service-types", response_model=list[ServiceTypeSchema])
def read_all_service_types():
    return ServiceTypeController.read_all_service_types()          

@service_type_router.delete("/")
def delete_service_type_by_id(service_type_id: str):
    return ServiceTypeController.delete_service_type_by_id(service_type_id)     

