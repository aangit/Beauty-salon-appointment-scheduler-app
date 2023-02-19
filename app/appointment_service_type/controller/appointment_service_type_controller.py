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

    # @staticmethod
    # def get_appointment_by_id(appointment_id: str):
    #     appointment = AppointmentServices.get_appointment_by_id(appointment_id) 
    #     if appointment:
    #         return appointment
    #     else:
    #         raise HTTPException(status_code=400, detail=f"Appointment with provided id {appointment_id} does not exist")

    @staticmethod
    def get_all_appointments_service_types():
        appointments_service_types = AppointmentServiceTypeServices.get_all_appointments_service_types()   
        return appointments_service_types

    # @staticmethod
    # def delete_appointment_by_id(appointment_id: str):
    #     try:
    #         AppointmentServices.delete_appointment_by_id(appointment_id)        
    #         return Response(content=f"Appointment with id - {appointment_id} is deleted")
    #     except Exception as e:
    #         raise HTTPException(status_code=400, detail=str(e))
