from datetime import date
from fastapi import APIRouter, Depends
from app.appointment.controller.appointment_controller import AppointmentController
from app.appointment.schemas import *
from app.appointment.schemas.schedule_appointment_schemas import *
from typing import Type
from app.appointment.models import Appointment
from app.user.controller.user_authenification_controller import JWTBearer

appointment_router = APIRouter(tags=["appointment"], prefix="/api/appointment")


@appointment_router.post("/add-new-appointment", response_model=AppointmentSchema)
def create_appointment(appointment: AppointmentSchemaIn):
    return AppointmentController.create_appointment(appointment.appointment_datetime, appointment.client_id, appointment.employee_id, appointment.service_types)    

@appointment_router.get("/id", response_model=AppointmentSchema)
def get_appointment_by_id(appointment_id: str):
    return AppointmentController.get_appointment_by_id(appointment_id) 

@appointment_router.get("/get-all-appointment-for-user", response_model= list[AppointmentSchema])
def get_appointments_by_client_id(client_id: str):
    return AppointmentController.get_appointments_by_client_id(client_id)


@appointment_router.get("/get-all-appointments-by-employee-and-status", response_model= list[AppointmentSchema])
def get_all_appointments_by_employee_id_and_status(employee_id: str, status_id):
    return AppointmentController.get_all_appointments_by_employee_id_and_status(employee_id, status_id)


@appointment_router.get("/get-all-pending-appointment-for-employee-for-date", response_model= list[AppointmentSchema])
def get_all_pending_appointments_by_employee_id_for_date(employee_id: str, status_id, appointment_datetime: str = None):
    return AppointmentController.get_all_pending_appointments_by_employee_id_for_date(employee_id, status_id, appointment_datetime)


@appointment_router.get("/get-all-appointments", response_model=list[AppointmentSchema])
def get_all_appointments():
    return AppointmentController.get_all_appointments()

@appointment_router.delete("/")
def delete_appointment_by_id(appointment_id: str):
    return AppointmentController.delete_appointment_by_id(appointment_id)

@appointment_router.put("/cancel-appointment", response_model = AppointmentSchema)
def cancel_appointement(appointment_id: str, credentials = Depends(JWTBearer("customer"))):
    return AppointmentController.cancel_appointement(appointment_id, credentials)

@appointment_router.put("/accept-appointment", response_model = AppointmentSchema)
def accept_appointment(appointment_id: str):
    return AppointmentController.accept_appointment(appointment_id)


@appointment_router.patch("/update-appointment", response_model = AppointmentSchema)
def update_appointment_by_id(appointment_id: str, appointment: UpdateAppointmentSchemaIn):
    return AppointmentController.update_appointment_by_id(appointment_id, appointment)
