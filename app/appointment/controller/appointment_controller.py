
from app.appointment.service import AppointmentServices
from fastapi import HTTPException, Response
from app.service_type.exceptions import ServiceTypeNotFound
from app.user.exceptions import  UserNotEmployee, UserNotClient, ClientNotFound, EmployeeNotFound, UserNotFound, UserNotAuthorized
from app.status.exceptions import StatusNotFoundException
from app.appointment.exceptions import AppointmentNotFound

class AppointmentController:
    @staticmethod
    def create_appointment(appointment_datetime, client_id, employee_id, service_types):
        try:
            appointment = AppointmentServices.create_appointment(appointment_datetime, client_id, employee_id, service_types ) 
            return appointment
        except ClientNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotClient as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except EmployeeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotEmployee as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except ServiceTypeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message) 
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def get_appointments_by_client_id(client_id: str, user_id: str):
        try:
            user_appointments = AppointmentServices.get_appointments_by_client_id(client_id, user_id)
            if user_appointments:
                return user_appointments
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotAuthorized as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotClient as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except AppointmentNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_appointments_by_employee_id_and_status(employee_id: str, status_id: str, user_id: str):
        try:
            employee_appointments = AppointmentServices.get_all_appointments_by_employee_id_and_status(employee_id, status_id, user_id)
            if employee_appointments:
                return employee_appointments
        except EmployeeNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotAuthorized as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotEmployee as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except AppointmentNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_appointments_by_employee_id_by_status_for_date(employee_id: str, status_id: str, user_id: str, appointment_datetime: str = None ):
        try:
            employee_appointments = AppointmentServices.get_all_appointments_by_employee_id_by_status_for_date(employee_id, status_id, user_id, appointment_datetime )
            if employee_appointments:
                return employee_appointments
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotAuthorized as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except AppointmentNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)


    @staticmethod
    def get_appointment_by_id(appointment_id: str):
        appointment = AppointmentServices.get_appointment_by_id(appointment_id) 
        if appointment:
            return appointment
        else:
            raise HTTPException(status_code=400, detail=f"Appointment with provided id {appointment_id} does not exist")

    @staticmethod
    def get_all_appointments():
        appointments = AppointmentServices.get_all_appointments()
        return appointments

    @staticmethod
    def delete_appointment_by_id(appointment_id: str):
        try:
            AppointmentServices.delete_appointment_by_id(appointment_id)        
            return Response(content=f"Appointment with id - {appointment_id} is deleted")
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def cancel_appointement(appointment_id: str, user_id: str):
        try:
            AppointmentServices.cancel_appointement(appointment_id, user_id)
            return Response(content=f"Appointment with id - {appointment_id} is canceled")
        except AppointmentNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotAuthorized as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    @staticmethod
    def accept_appointment(appointment_id: str, user_id: str):
        try:
            AppointmentServices.accept_appointment(appointment_id, user_id)
            return Response(content=f"Appointment with id - {appointment_id} is accepted")
        except AppointmentNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotAuthorized as e:
            raise HTTPException(status_code=e.code, detail=e.message)         
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))


    @staticmethod
    def update_appointment_by_id(appointment_id: str, appointment, user_id: str):
        try:
            AppointmentServices.update_appointment_by_id(appointment_id, appointment, user_id)        
            return Response(content=f"Appointment with id - {appointment_id} is updated")
        except AppointmentNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotAuthorized as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except UserNotFound as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except StatusNotFoundException as e:
            raise HTTPException(status_code=e.code, detail=e.message)
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))
