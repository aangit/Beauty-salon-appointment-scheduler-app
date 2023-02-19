from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.appointment_service_type.models import AppointmentServiceType


class AppointmentServiceTypeRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_appointment_service_type(self, appointment_id, service_type_id):
        try:
            appointment_service_type = AppointmentServiceType(appointment_id, service_type_id)
            self.db.add(appointment_service_type)
            self.db.commit()
            self.db.refresh(appointment_service_type)
            return appointment_service_type
        except IntegrityError as e:
            raise e


    def get_all_appointments_service_types(self):
        appointments_service_types = self.db.query(AppointmentServiceType).all()
        return appointments_service_types

