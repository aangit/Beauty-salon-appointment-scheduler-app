from sqlalchemy.exc import IntegrityError
from app.appointment_service_type.service import AppointmentServiceTypeServices
from fastapi import HTTPException

class AppointmentServiceTypeController:
    @staticmethod
    def create_appointment_service_type(appointment_id, service_type_id):
        """
        It creates an appointment service type
        
        :param appointment_id
        :param service_type_id
        :return: The appointment_service_type is being returned.
        """
        try:
            appointment_service_type = AppointmentServiceTypeServices.create_appointment_service_type(appointment_id, service_type_id)
            return appointment_service_type
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"Appointment {appointment_id} with {service_type_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_appointments_service_types():
        """
        It returns a list of dictionaries, each dictionary containing the following keys: 
        'appointment_service_type_id', 'appointment_service_type_name',
        'appointment_service_type_description', 'appointment_service_type_price',
        'appointment_service_type_duration', 'appointment_service_type_duration_unit',
        'appointment_service_type_is_active', 'appointment_service_type_is_deleted',
        'appointment_service_type_created_at', 'appointment_service_type_updated_at'
        :return: A list of dictionaries.
        """
        appointments_service_types = AppointmentServiceTypeServices.get_all_appointments_service_types()   
        return appointments_service_types

