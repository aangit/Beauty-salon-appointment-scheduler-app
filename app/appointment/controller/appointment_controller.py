
from app.appointment.service import AppointmentServices
from fastapi import HTTPException, Response
from app.service_type.exceptions import ServiceTypeNotFound
from app.user.exceptions import  UserNotEmployee, UserNotClient, ClientNotFound, EmployeeNotFound, UserNotFound, UserNotAuthorized
from app.status.exceptions import StatusNotFoundException
from app.appointment.exceptions import AppointmentNotFound

class AppointmentController:
    @staticmethod
    def create_appointment(appointment_datetime, client_id, employee_id, service_types):
        """
        It creates an appointment, and if it fails, it raises an HTTPException with the appropriate
        status code and message
        
        :param appointment_datetime: datetime
        :param client_id: the id of the client
        :param employee_id: int
        :param service_types
        :return: The appointment object
        """
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
        """
        It gets the appointments by client id and checks if the client is authorized to perform an action by login credentials - user id
        
        :param client_id: str
        :type client_id: str
        :param user_id: str
        :type user_id: str
        :return: A list of appointments
        """
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
        """
        It gets all appointments by employee id and status and checks if the employee is authorized to perform an action by login credentials - user id 
        
        :param employee_id: str, status_id: str, user_id: str
        :type employee_id: str
        :param status_id: str
        :type status_id: str
        :param user_id: str
        :type user_id: str
        :return: A list of appointments
        """
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
        """
        It returns a list of appointments for a given employee, status, and date and checks if the employee is authorized to perform an action by login credentials - user id 
        
        :param employee_id: str, status_id: str, user_id: str, appointment_datetime: str = None
        :type employee_id: str
        :param status_id: str = "1"
        :type status_id: str
        :param user_id: str = None,
        :type user_id: str
        :param appointment_datetime: str = None
        :type appointment_datetime: str
        :return: A list of appointments
        """
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
        """
        If the appointment exists, return it, otherwise raise an exception
        
        :param appointment_id: str
        :type appointment_id: str
        :return: The appointment object
        """
        appointment = AppointmentServices.get_appointment_by_id(appointment_id) 
        if appointment:
            return appointment
        else:
            raise HTTPException(status_code=400, detail=f"Appointment with provided id {appointment_id} does not exist")

    @staticmethod
    def get_all_appointments():
        """
        It returns all appointments from the database
        :return: A list of dictionaries
        """
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
        """
        It cancels an appointment with the given appointment_id and and checks if the client is authorized to perform an action by login credentials - user id 
        
        :param appointment_id: str, user_id: str
        :type appointment_id: str
        :param user_id: str
        :type user_id: str
        :return: Response(content=f"Appointment with id - {appointment_id} is canceled")
        """
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
        """
        It accepts an appointment_id and checks if the employee is authorized to perform an action by login credentials - user id , and if the appointment is found, it is accepted
        
        :param appointment_id: str, user_id: str
        :type appointment_id: str
        :param user_id: str - the user id of the user who is accepting the appointment
        :type user_id: str
        :return: Response(content=f"Appointment with id - {appointment_id} is accepted")
        """
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
        """
        It updates an appointment by id, and if it fails, it raises an HTTPException with the
        appropriate status code and message
        
        :param appointment_id: str
        :type appointment_id: str
        :param appointment: Appointment
        :param user_id: str
        :type user_id: str
        """
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
