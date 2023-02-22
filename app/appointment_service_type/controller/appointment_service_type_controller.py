from sqlalchemy.exc import IntegrityError
from app.appointment_service_type.service import AppointmentServiceTypeServices
from fastapi import HTTPException

class AppointmentServiceTypeController:
    @staticmethod
    def create_appointment_service_type(appointment_id, service_type_id):
        try:
            appointment_service_type = AppointmentServiceTypeServices.create_appointment_service_type(appointment_id, service_type_id)
            return appointment_service_type
        except IntegrityError as e:
            raise HTTPException(status_code=400, detail=f"Appointment {appointment_id} with {service_type_id} already exists.")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def get_all_appointments_service_types():
        appointments_service_types = AppointmentServiceTypeServices.get_all_appointments_service_types()   
        return appointments_service_types

