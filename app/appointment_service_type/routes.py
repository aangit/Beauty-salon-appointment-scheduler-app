from fastapi import APIRouter
from app.appointment_service_type.controller import AppointmentServiceTypeController
from app.appointment_service_type.schemas import *

appointment_service_type_router = APIRouter(tags=["appointment_service_type"], prefix="/api/appointment_service_type")


@appointment_service_type_router.post("/add-new-appointment", response_model=AppointmentServiceTypeSchema)
def create_appointment_service_type(appointment_service_type: AppointmentServiceTypeSchemaIn):
    return AppointmentServiceTypeController.create_appointment_service_type(appointment_service_type.appointment_id, appointment_service_type.service_type_id)       


@appointment_service_type_router.get("/get-all-appointment_service_types", response_model=list[AppointmentServiceTypeSchema])
def get_all_appointments_service_types():
    return AppointmentServiceTypeController.get_all_appointments_service_types()        

