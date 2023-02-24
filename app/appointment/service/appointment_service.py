
from app.appointment.models.appointment_models import Appointment
from app.appointment_service_type.repository.appointment_service_type_repository import AppointmentServiceTypeRepository
from app.db.database import SessionLocal
from app.appointment.repository.appointment_repository import AppointmentRepository
from app.appointment.schemas import UpdateAppointmentSchemaIn
from fastapi.encoders import jsonable_encoder
from app.status.exceptions import StatusNotFoundException
from app.status.repository import StatusRepository
from app.user.repository import UserRepository
from app.user.exceptions import UserNotEmployee, UserNotClient, ClientNotFound, EmployeeNotFound, UserNotFound, UserNotAuthorized
from typing import List, Type
from app.service_type.exceptions import ServiceTypeNotFound
from app.appointment.exceptions import AppointmentNotFound


class AppointmentServices:

    @staticmethod
    def create_appointment(appointment_datetime, client_id, employee_id, service_types: List[str]):
        """
        It creates an appointment, and then creates a relationship between the appointment and the
        service types.
        
        :param appointment_datetime: datetime.datetime
        :param client_id: 1
        :param employee_id: 1
        :param service_types: List[str]
        :type service_types: List[str]
        :return: The appointment object
        """
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
    def get_appointments_by_client_id(client_id: str, user_id: str) -> Type[Appointment]:
        """
        It gets all appointments for a client by client id and checks if the client is authorized to perform an action by login credentials - user id
        
        :param client_id: str, user_id: str
        :type client_id: str
        :param user_id: str = the user id of the user who is making the request
        :type user_id: str
        :return: A list of Appointment objects.
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                user = user_repository.get_user_by_id(client_id)
                if user is None:
                    raise UserNotFound(message="User with provided id does not exist", code=404)
                if user.id != user_id:
                    raise UserNotAuthorized(message="User is not authorized to access data.", code=401)
                if user.user_type.user_type != "customer":
                    raise UserNotClient(
                        message="Unknown user.", code=400)
                appointment_repository = AppointmentRepository(db)
                appointments = appointment_repository.get_appointments_by_client_id(
                    client_id)
                if not appointments:
                    raise AppointmentNotFound(message="This user has no appointments.", code=404)
                
                return appointments

            except Exception as e:
                raise e

    @staticmethod
    def get_all_appointments_by_employee_id_and_status(employee_id: str, status_id: str, user_id: str ) -> Type[Appointment]:
        """
        It gets all appointments by employee id and status and checks if the employee is authorized to perform an action by login credentials - user id
        
        :param employee_id: str, status_id: str, user_id: str
        :type employee_id: str
        :param status_id: str
        :type status_id: str
        :param user_id: str = the user id of the user making the request
        :type user_id: str
        :return: A list of Appointment objects.
        """
        with SessionLocal() as db:
            try:
                user_repository = UserRepository(db)
                employee_user = user_repository.get_user_by_id(employee_id)
                if not employee_user:
                    raise EmployeeNotFound(message="Employee not found", code=404)
                if employee_user.id != user_id:
                    raise UserNotAuthorized(message="User is not authorized to access data.", code=401)
                if employee_user.user_type.user_type != "employee":
                    raise UserNotEmployee(message="User is not an employee.", code=404)
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                status = status_repository.read_status_by_id(status_id)
                if not status:
                    raise StatusNotFoundException(message="Requested status not found.", code=404)
                appointments = appointment_repository.get_all_appointments_by_employee_id_and_status(
                    employee_id, status_id)
                if not appointments:
                    raise AppointmentNotFound(message="This user has no appointments.", code=404)
                return appointments
            except Exception as e:
                raise e

    @staticmethod
    def get_all_appointments_by_employee_id_by_status_for_date(employee_id: str, status_id: str, user_id: str ,appointment_datetime: str = None ) -> Type[Appointment]:
        """
        This function returns all appointments for a given employee, status, and date and checks if the employee is authorized to perform an action by login credentials - user id
        
        :param employee_id: str, status_id: str, user_id: str ,appointment_datetime: str = None
        :type employee_id: str
        :param status_id: str = "1"
        :type status_id: str
        :param user_id: str = the user id of the user who is making the request
        :type user_id: str
        :param appointment_datetime: str = None
        :type appointment_datetime: str
        :return: A list of appointments
        """
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                status_repository = StatusRepository(db)
                user_repository = UserRepository(db)
                employee = user_repository.get_user_by_id(employee_id)
                if employee is None:
                    raise UserNotFound(message="User not found.", code=404)
                if employee_id != user_id:
                    raise UserNotAuthorized(message="User is not authorized to access data.", code=401)
                id_status = status_repository.read_status_by_id(status_id)
                if id_status is None:
                    raise StatusNotFoundException(message="Requested status not found.", code=404)
                status_id = id_status.id
                appointments = appointment_repository.get_all_appointments_by_employee_id_by_status_for_date(
                    employee_id, status_id, appointment_datetime)
                if not appointments:
                    raise AppointmentNotFound(message="This user has no appointments.", code=404)
                return appointments
            except Exception as e:
                raise e

    @staticmethod
    def get_appointment_by_id(appointment_id: str):
        """
        It gets an appointment by id
        
        :param appointment_id: str
        :type appointment_id: str
        :return: A list of Appointment objects
        """
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                return appointment_repository.get_appointment_by_id(appointment_id)
            except Exception as e:
                raise e

    @staticmethod
    def get_all_appointments():
        """
        It creates a database session, creates an appointment repository, and then calls the
        get_all_appointments() function on the repository.
        :return: A list of Appointment objects
        """
        with SessionLocal() as db:
            appointment_repository = AppointmentRepository(db)
            return appointment_repository.get_all_appointments()

    @staticmethod
    def delete_appointment_by_id(appointment_id: str):
        """
        It deletes an appointment from the database by its id.
        
        :param appointment_id: str
        :type appointment_id: str
        :return: The return value is the number of rows deleted.
        """
        try:
            with SessionLocal() as db:
                appointment_repository = AppointmentRepository(db)
                return appointment_repository.delete_appointment_by_id(appointment_id)
        except Exception as e:
            raise e

    @staticmethod
    def cancel_appointement(appointment_id: str, user_id: str):
        """
        It cancels an appointment if the appointment exists and if the client is authorized to cancel it
        
        :param appointment_id: str
        :type appointment_id: str
        :param user_id: str
        :type user_id: str
        :return: The return value is the result of the cancel_appointement method.
        """
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                appointment = appointment_repository.get_appointment_by_id(
                    appointment_id)
                if not appointment:
                    raise AppointmentNotFound(message="Appointment not found.", code=404)
                if appointment.client_id != user_id:
                    raise UserNotAuthorized(message="User is not authorized to access data.", code=401)
                return appointment_repository.cancel_appointement(appointment_id)
            except Exception as e:
                raise e


    @staticmethod
    def accept_appointment(appointment_id: str, user_id: str):
        """
        It accepts an appointment_id and user_id, checks if the appointment exists, if it does, it
        checks if the user is authorized to access the appointment, if the user is authorized, it
        returns the appointment.
        
        :param appointment_id: str
        :type appointment_id: str
        :param user_id: str = the id of the user who is accepting the appointment
        :type user_id: str
        :return: The return value is the result of the accept_appointment method.
        """
        with SessionLocal() as db:
            try:
                appointment_repository = AppointmentRepository(db)
                appointment = appointment_repository.get_appointment_by_id(
                    appointment_id)
                if not appointment:
                    raise AppointmentNotFound(message="Appointment not found.", code=404)
                if appointment.employee_id != user_id:
                     raise UserNotAuthorized(message="User is not authorized to access data.", code=401)
                return appointment_repository.accept_appointment(appointment_id)
            except Exception as e:
                raise e

    @staticmethod
    def update_appointment_by_id(appointment_id: str, appointment, user_id: str):
        """
        It takes an appointment_id, appointment, and user_id (checks if the user is authorized to access the appointment, if the user is authorized, it
        updates the appointment) as parameters, and returns an updated appointment.

        :param appointment_id: str
        :type appointment_id: str
        :param appointment: AppointmentCreate
        :param user_id: str 
        :type user_id: str
        :return: The return value is the updated appointment.
        """
        try:
            with SessionLocal() as db:
                appointment_repository = AppointmentRepository(db)
                user_repository = UserRepository(db)
                status_repository = StatusRepository(db)
                stored_appointment_data = appointment_repository.get_appointment_by_id(
                    appointment_id)
                if not stored_appointment_data:
                    raise AppointmentNotFound(message="Appointment not found.", code=404)
                if stored_appointment_data.employee_id != user_id:
                    raise UserNotAuthorized(message="User is not authorized to access data.", code=401)
                if appointment.client_id and not user_repository.get_user_by_id(appointment.client_id):
                    raise UserNotFound(message="Client not found.", code=404)
                if appointment.employee_id and not user_repository.get_user_by_id(appointment.employee_id):
                    raise UserNotFound(message="Employee not found.", code=404)
                if appointment.status_id and not status_repository.read_status_by_id(appointment.status_id):
                    raise StatusNotFoundException(message="Status not found.", code=404)
                stored_appointment_model = UpdateAppointmentSchemaIn(
                    **jsonable_encoder(stored_appointment_data))
                update_data = appointment.dict(exclude_unset=True)
                updated_appointment = stored_appointment_model.copy(
                    update=update_data)
                return appointment_repository.update_appointment_by_id(appointment_id, updated_appointment.appointment_datetime, updated_appointment.client_id, updated_appointment.employee_id, updated_appointment.status_id)
        except Exception as e:
            raise e
