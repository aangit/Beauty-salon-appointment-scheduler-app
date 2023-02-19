
from datetime import date, datetime
from app import appointment
from app.appointment.models.appointment_models import Appointment
from app.appointment_service_type.repository.appointment_service_type_repository import AppointmentServiceTypeRepository
from app.db.database import SessionLocal
from app.appointment.repository.appointment_repository import AppointmentRepository
from app.appointment.schemas import UpdateAppointmentSchemaIn
from fastapi.encoders import jsonable_encoder
from app.service_type.models.service_type_models import ServiceType
from app.service_type.repository import ServiceTypeRepository
from app.status.repository import StatusRepository
from app.user.repository.user_repository import UserRepository
from typing import List, Type

class AppointmentServices:

    @staticmethod
    def create_appointment(appointment_datetime , client_id, employee_id, service_types: List[str]):
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                pending_status = status_repository.read_status_by_name("pending")
                pending_status_id = pending_status.id
                appointment = appointment_repository.create_appointment(appointment_datetime, client_id, employee_id, pending_status_id)
                appointment_service_repository = AppointmentServiceTypeRepository(db)
                for service_type_id in service_types:
                    appointment_service_repository.create_appointment_service_type(appointment.id, service_type_id)
                db.refresh(appointment)
                return appointment      
            except Exception as e:
                raise e


    @staticmethod
    def get_appointments_by_client_id(client_id: str) -> Type[Appointment]:
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                appointments= appointment_repository.get_appointments_by_client_id(client_id)
                return appointments
                
            except Exception as e:
                raise e

    @staticmethod
    def get_all_appointments_by_employee_id_and_status(employee_id: str, status_id: str) -> Type[Appointment]:
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                _ = status_repository.read_status_by_id(status_id)
                appointments = appointment_repository.get_all_appointments_by_employee_id_and_status(employee_id, status_id)
                return appointments
            except Exception as e:
                raise e

    @staticmethod
    def get_all_pending_appointments_by_employee_id_for_date(employee_id: str, status_id: str, appointment_datetime: str =None) -> Type[Appointment]:
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                rejected_status = status_repository.read_status_by_name("pending")
                status_id = rejected_status.id
                appointments = appointment_repository.get_all_pending_appointments_by_employee_id_for_date(employee_id, status_id, appointment_datetime)
                return appointments
            except Exception as e:
                raise e


    @staticmethod
    def get_appointment_by_id(appointment_id: str):
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                return appointment_repository.get_appointment_by_id(appointment_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_appointments():
        with SessionLocal() as db:
            appointment_repository = AppointmentRepository(db)
            return appointment_repository.get_all_appointments()     

    @staticmethod
    def delete_appointment_by_id(appointment_id: str):
        try:
            with SessionLocal() as db:
                appointment_repository = AppointmentRepository(db)
                return appointment_repository.delete_appointment_by_id(appointment_id)
        except Exception as e:
            raise e

    @staticmethod
    def cancel_appointement(appointment_id: str, user_id: str):
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                appointment = appointment_repository.get_appointment_by_id(appointment_id)
                if appointment.client_id != user_id:
                    raise ValueError("User is not authorized to cancel this appointment")
                return appointment_repository.cancel_appointement(appointment_id)
            except Exception as e:
                raise e

    @staticmethod
    def accept_appointment(appointment_id: str):
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                return appointment_repository.accept_appointment(appointment_id)
            except Exception as e:
                raise e


    @staticmethod
    def update_appointment_by_id(appointment_id: str, appointment):
        try:
            with SessionLocal() as db:
                appointment_repository = AppointmentRepository(db)
                stored_appointment_data = appointment_repository.get_appointment_by_id(appointment_id)
                stored_appointment_model = UpdateAppointmentSchemaIn(**jsonable_encoder(stored_appointment_data))
                update_data = appointment.dict(exclude_unset=True)
                updated_appointment = stored_appointment_model.copy(update=update_data)
                return appointment_repository.update_appointment_by_id(appointment_id, updated_appointment.appointment_datetime,updated_appointment.client_id, updated_appointment.employee_id, updated_appointment.status_id)
        except Exception as e:
            print(e)
            raise e
