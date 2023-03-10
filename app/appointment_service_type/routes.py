from fastapi import APIRouter, Depends
from app.appointment_service_type.controller import AppointmentServiceTypeController
from app.appointment_service_type.schemas import *
from app.user.controller.user_authenification_controller import JWTBearer

appointment_service_type_router = APIRouter(tags=["appointment-service-type"], prefix="/api/appointment-service-type")


@appointment_service_type_router.post("/add-new-appointment-service-type", response_model=AppointmentServiceTypeSchema, dependencies=[Depends(JWTBearer("super_user"))])
def create_appointment_service_type(appointment_service_type: AppointmentServiceTypeSchemaIn):
    """
    It takes an appointment_service_type object, and passes the appointment_id and service_type_id to
    the controller
    
    :param appointment_service_type: AppointmentServiceTypeSchemaIn
    :type appointment_service_type: AppointmentServiceTypeSchemaIn
    :return: The return value is a tuple of (AppointmentServiceType, bool)
    """
    return AppointmentServiceTypeController.create_appointment_service_type(appointment_service_type.appointment_id, appointment_service_type.service_type_id)       


@appointment_service_type_router.get("/get-all-appointment_service_types", response_model=list[AppointmentServiceTypeSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_appointments_service_types():
    """
    It returns a list of all the appointment service types in the database
    :return: A list of AppointmentServiceType objects
    """
    return AppointmentServiceTypeController.get_all_appointments_service_types()        

