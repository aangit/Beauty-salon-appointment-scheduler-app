from app.db.database import SessionLocal
from app.appointment_service_type.repository import AppointmentServiceTypeRepository

class AppointmentServiceTypeServices:

    @staticmethod
    def create_appointment_service_type(appointment_id, service_type_id):
        with SessionLocal() as db:
            try:
                appointments_service_types_repository = AppointmentServiceTypeRepository(db)
                return appointments_service_types_repository.create_appointment_service_type(appointment_id, service_type_id)              
            except Exception as e:
                raise e


    @staticmethod
    def get_all_appointments_service_types():
        with SessionLocal() as db:
            appointments_service_types_repository = AppointmentServiceTypeRepository(db)
            return appointments_service_types_repository.get_all_appointments_service_types()    

