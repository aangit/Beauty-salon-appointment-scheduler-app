from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.appointment_service_type.models import AppointmentServiceType


class AppointmentServiceTypeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_appointment_service_type(self, appointment_id, service_type_id):
        """
        It creates an appointment_service_type object, adds it to the database, commits the changes, and
        returns the object.
        
        :param appointment_id
        :param service_type_id
        :return: The appointment_service_type object
        """
        try:
            appointment_service_type = AppointmentServiceType(appointment_id, service_type_id)
            self.db.add(appointment_service_type)
            self.db.commit()
            self.db.refresh(appointment_service_type)
            return appointment_service_type
        except IntegrityError as e:
            raise e


    def get_all_appointments_service_types(self):
        """
        It returns all the appointment service types from the database
        :return: A list of AppointmentServiceType objects.
        """
        appointments_service_types = self.db.query(AppointmentServiceType).all()
        return appointments_service_types

