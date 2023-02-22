from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class AppointmentServiceType(Base):
    __tablename__ = "appointmentservicetype"

    appointment_id = Column(String(45), ForeignKey("appointment.id"), primary_key = True, autoincrement = False)
    appointment = relationship("Appointment", lazy='subquery')

    service_type_id = Column(String(45), ForeignKey("servicetype.id"), primary_key = True, autoincrement = False)
    service_type = relationship("ServiceType", lazy='subquery')   

    def __init__(self, appointment_id, service_type_id):
        self.appointment_id = appointment_id
        self.service_type_id = service_type_id