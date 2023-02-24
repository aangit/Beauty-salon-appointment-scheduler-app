from app.db.database import SessionLocal
from app.appointment_service_type.repository import AppointmentServiceTypeRepository

class AppointmentServiceTypeServices:

    @staticmethod
    def create_appointment_service_type(appointment_id, service_type_id):
        """
        It creates an appointment_service_type record in the database.
        
        :param appointment_id
        :param service_type_id
        :return: The return value is the appointment_service_type_id
        """
        with SessionLocal() as db:
            try:
                appointments_service_types_repository = AppointmentServiceTypeRepository(db)
                return appointments_service_types_repository.create_appointment_service_type(appointment_id, service_type_id)              
            except Exception as e:
                raise e


    @staticmethod
    def get_all_appointments_service_types():
        """
        It gets all the appointment service types from the database.
        :return: A list of AppointmentServiceType objects
        """
        with SessionLocal() as db:
            appointments_service_types_repository = AppointmentServiceTypeRepository(db)
            return appointments_service_types_repository.get_all_appointments_service_types()    

