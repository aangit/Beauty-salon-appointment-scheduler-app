
from app.appointment.models.appointment_models import Appointment
from app.appointment_service_type.repository.appointment_service_type_repository import AppointmentServiceTypeRepository
from app.db.database import SessionLocal
from app.appointment.repository.appointment_repository import AppointmentRepository
from app.appointment.schemas import UpdateAppointmentSchemaIn
from fastapi.encoders import jsonable_encoder
from app.status.exceptions import StatusNotFoundException
from app.status.repository import StatusRepository
from app.user.repository import UserRepository
from app.user.exceptions import UserNotEmployee, UserNotClient, ClientNotFound, EmployeeNotFound, UserNotFound
from typing import List, Type
from app.service_type.exceptions import ServiceTypeNotFound



class AppointmentServices:

    @staticmethod
    def create_appointment(appointment_datetime, client_id, employee_id, service_types: List[str]):
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                client_user = user_repository.get_user_by_id(client_id)
                if client_user is None:
                    raise ClientNotFound(message="Client not found", code=404)
                if client_user.user_type.user_type != "customer":
                    raise UserNotClient(
                        message="User is not a client.", code=404)
                employee_user = user_repository.get_user_by_id(employee_id)
                if employee_user is None:
                    raise EmployeeNotFound(
                        message="Employee not found", code=404)
                if employee_user.user_type.user_type != "employee":
                    raise UserNotEmployee(
                        message="User is not an employee.", code=404)
                employee_service_types = [
                    str(service_type.id) for service_type in employee_user.service_types]
                for service_type_id in service_types:
                    if service_type_id not in employee_service_types:
                        raise ServiceTypeNotFound(
                            message="Requested service type is not available.", code=404)
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                pending_status = status_repository.read_status_by_name(
                    "pending")
                pending_status_id = pending_status.id
                appointment = appointment_repository.create_appointment(
                    appointment_datetime, client_id, employee_id, pending_status_id)
                appointment_service_repository = AppointmentServiceTypeRepository(
                    db)
                for service_type_id in service_types:
                    appointment_service_repository.create_appointment_service_type(
                        appointment.id, service_type_id)
                db.refresh(appointment)
                return appointment
            except Exception as e:
                raise e

    @staticmethod
    def get_appointments_by_client_id(client_id: str) -> Type[Appointment]:
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_id(client_id)
                if not user:
                    raise UserNotFound(message=f"User with provided id {client_id} does not exist", code=404)
                if user.user_type.user_type != "customer":
                    raise UserNotClient(
                        message="Unknown user.", code=400)
                appointment_repository = AppointmentRepository(db)
                appointments = appointment_repository.get_appointments_by_client_id(
                    client_id)
                return appointments

            except Exception as e:
                raise e

    @staticmethod
    def get_all_appointments_by_employee_id_and_status(employee_id: str, status_id: str) -> Type[Appointment]:
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                employee_user = user_repository.get_user_by_id(employee_id)
                if not employee_user:
                    raise EmployeeNotFound(message="Employee not found", code=404)
                if employee_user.user_type.user_type != "employee":
                    raise UserNotEmployee(message="User is not an employee.", code=404)
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                status = status_repository.read_status_by_id(status_id)
                if not status:
                    raise StatusNotFoundException(message="Requested status not found.", code=404)
                appointments = appointment_repository.get_all_appointments_by_employee_id_and_status(
                    employee_id, status_id)
                return appointments
            except Exception as e:
                raise e

    @staticmethod
    def get_all_pending_appointments_by_employee_id_for_date(employee_id: str, status_id: str, appointment_datetime: str = None) -> Type[Appointment]:
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                id_status = status_repository.read_status_by_id(status_id)
                status_id = id_status.id
                appointments = appointment_repository.get_all_pending_appointments_by_employee_id_for_date(
                    employee_id, status_id, appointment_datetime)
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
                appointment = appointment_repository.get_appointment_by_id(
                    appointment_id)
                if appointment.client_id != user_id:
                    raise ValueError(
                        "User is not authorized to cancel this appointment")
                return appointment_repository.cancel_appointement(appointment_id)
            except Exception as e:
                raise e

    @staticmethod
    def accept_appointment(appointment_id: str, user_id: str):
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                appointment = appointment_repository.get_appointment_by_id(
                    appointment_id)
                if appointment.employee_id != user_id:
                    raise ValueError(
                        "User is not authorized to cancel this appointment")
                return appointment_repository.accept_appointment(appointment_id)
            except Exception as e:
                raise e

    @staticmethod
    def update_appointment_by_id(appointment_id: str, appointment):
        try:
            with SessionLocal() as db:
                appointment_repository = AppointmentRepository(db)
                stored_appointment_data = appointment_repository.get_appointment_by_id(
                    appointment_id)
                stored_appointment_model = UpdateAppointmentSchemaIn(
                    **jsonable_encoder(stored_appointment_data))
                update_data = appointment.dict(exclude_unset=True)
                updated_appointment = stored_appointment_model.copy(
                    update=update_data)
                return appointment_repository.update_appointment_by_id(appointment_id, updated_appointment.appointment_datetime, updated_appointment.client_id, updated_appointment.employee_id, updated_appointment.status_id)
        except Exception as e:
            raise e
