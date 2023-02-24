
from fastapi import APIRouter, Depends
from app.appointment.controller.appointment_controller import AppointmentController
from app.appointment.schemas import *

from app.user.controller.user_authenification_controller import JWTBearer

appointment_router = APIRouter(tags=["appointment"], prefix="/api/appointment")


@appointment_router.post("/add-new-appointment", response_model=AppointmentSchema, dependencies=[Depends(JWTBearer(["super_user", "employee", "customer"]))])
def create_appointment(appointment: AppointmentSchemaIn):
    """
    Create an appointment with the given appointment datetime, client id, employee id, and service types
    
    :param appointment: AppointmentSchemaIn
    :type appointment: AppointmentSchemaIn
    :return: The return value is a tuple of (appointment_id, appointment_datetime, client_id,
    employee_id, service_types)
    """
    return AppointmentController.create_appointment(appointment.appointment_datetime, appointment.client_id, appointment.employee_id, appointment.service_types)    

@appointment_router.get("/id", response_model=AppointmentSchema, dependencies=[Depends(JWTBearer(["super_user", "employee"]))])
def get_appointment_by_id(appointment_id: str):
    """
    Get an appointment by its id
    
    :param appointment_id: str
    :type appointment_id: str
    :return: A dictionary of the appointment
    """
    return AppointmentController.get_appointment_by_id(appointment_id) 

@appointment_router.get("/get-all-appointments-for-user", response_model= list[AppointmentSchema]) 
def get_appointments_by_client_id(client_id: str, credentials = Depends(JWTBearer("customer"))):
    """
    It returns a list of appointments for a given client_id, but only if the client_id matches the
    user_id in the JWT token
    
    :param client_id: str 
    :type client_id: str
    :param credentials: The JWT token that is passed in the header of the request
    :return: A list of appointments
    """
    return AppointmentController.get_appointments_by_client_id(client_id, credentials["user_id"])


@appointment_router.get("/get-all-appointments-by-employee-and-status", response_model= list[AppointmentSchema]) 
def get_all_appointments_by_employee_id_and_status(employee_id: str, status_id, credentials = Depends(JWTBearer("employee"))):
    """
    It returns a list of appointments for a given employee_id and status_id but only if the employee_id matches the
    user_id in the JWT token
    
    :param employee_id: str 
    :type employee_id: str
    :param status_id: int
    :param credentials: This is the JWT token that is passed in the header of the request
    :return: A list of appointments
    """
    return AppointmentController.get_all_appointments_by_employee_id_and_status(employee_id, status_id, credentials["user_id"])


@appointment_router.get("/get-all-appointment-for-employee-by-status-for-date", response_model= list[AppointmentSchema])
def get_all_appointments_by_employee_id_by_status_for_date(employee_id: str, status_id, appointment_datetime: str = None, credentials = Depends(JWTBearer("employee"))):
    """
    `get_all_appointments_by_employee_id_by_status_for_date` returns all appointments for a given
    employee, status, and date but only if the employee_id matches the user_id in the JWT token
    
    :param employee_id: str = None,
    :type employee_id: str
    :param status_id: int
    :param appointment_datetime: str = None
    :type appointment_datetime: str
    :param credentials: This is the JWT token that is passed in the header of the request
    :return: A list of appointments
    """
    return AppointmentController.get_all_appointments_by_employee_id_by_status_for_date(employee_id, status_id, credentials["user_id"], appointment_datetime )


@appointment_router.get("/get-all-appointments", response_model=list[AppointmentSchema], dependencies=[Depends(JWTBearer("super_user"))])
def get_all_appointments():
    """
    It returns all appointments from the database
    :return: A list of all appointments
    """
    return AppointmentController.get_all_appointments()

@appointment_router.delete("/", dependencies=[Depends(JWTBearer("super_user"))])
def delete_appointment_by_id(appointment_id: str):
    """
    Delete an appointment by id
    
    :param appointment_id: str
    :type appointment_id: str
    :return: The return value of the function is the return value of the function that is being called.
    """
    return AppointmentController.delete_appointment_by_id(appointment_id)

@appointment_router.put("/cancel-appointment", response_model = AppointmentSchema)
def cancel_appointement(appointment_id: str, credentials = Depends(JWTBearer("customer"))):
    """
    It takes an appointment_id and a JWT token as input, and returns the result of the
    cancel_appointement function in the AppointmentController class
    
    :param appointment_id: str 
    :type appointment_id: str
    :param credentials: This is the JWT token that is passed in the header of the request
    :return: A dictionary with the following keys:
    - status: The status of the request
    - message: A message to be displayed to the user
    - data: The data to be displayed to the user
    """
    return AppointmentController.cancel_appointement(appointment_id, credentials["user_id"])

@appointment_router.put("/accept-appointment", response_model = AppointmentSchema)
def accept_appointment(appointment_id: str, credentials = Depends(JWTBearer("employee"))):
    """
    It accepts an appointment_id and a credentials object, which is a dependency that is resolved by the
    JWTBearer function
    
    :param appointment_id: str - The appointment ID
    :type appointment_id: str
    :param credentials: The JWT token that is passed in the header of the request
    :return: The return value is a tuple of the form (status_code, response_object)
    """
    return AppointmentController.accept_appointment(appointment_id, credentials["user_id"])


@appointment_router.patch("/update-appointment", response_model = AppointmentSchema) 
def update_appointment_by_id(appointment_id: str, appointment: UpdateAppointmentSchemaIn, credentials = Depends(JWTBearer("employee"))):
    """
    It takes an appointment_id, an appointment object, and a credentials object, and returns the result
    of calling the update_appointment_by_id function on the AppointmentController class, passing in the
    appointment_id, appointment, and credentials["user_id"] as arguments but only if the employee_id matches the user_id in the JWT token
    
    :param appointment_id: str - The ID of the appointment to update
    :type appointment_id: str
    :param appointment: UpdateAppointmentSchemaIn
    :type appointment: UpdateAppointmentSchemaIn
    :param credentials: The JWT token that is passed in the header
    :return: The return value is a tuple of (response, status_code)
    """
    return AppointmentController.update_appointment_by_id(appointment_id, appointment, credentials["user_id"])
