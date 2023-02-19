from email.policy import default
from http import client
from app.db.database import Base
from sqlalchemy import Column, String, ForeignKey, DateTime
from uuid import uuid4
from sqlalchemy.orm import relationship



class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    appointment_datetime = Column(DateTime)
    

    client_id = Column(String(45), ForeignKey("user.id"))
    client = relationship("User", lazy='subquery', foreign_keys=client_id )

    employee_id = Column(String(45), ForeignKey("user.id"))
    employee = relationship("User", lazy='subquery', foreign_keys=employee_id)   

    status_id = Column(String(50), ForeignKey("status.id"))
    status = relationship("Status", lazy = 'subquery')

    service_types = relationship('ServiceType', secondary='appointmentservicetype', back_populates='appointments', lazy = 'subquery')

    def __init__(self, appointment_datetime, client_id, employee_id, status_id):
        self.appointment_datetime = appointment_datetime
        self.client_id = client_id
        self.employee_id = employee_id
        self.status_id = status_id
     