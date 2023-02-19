from sqlite3 import Time
from sqlalchemy.orm import relationship
from app.db.database import Base
from sqlalchemy import Column, String, Time, Float, DateTime
from uuid import uuid4

class ServiceType(Base):
    __tablename__ = "servicetype"
    id = Column(String(50), primary_key=True, default=uuid4, autoincrement=False)
    service_name = Column(String(100))
    approximate_duration = Column(Time)
    price = Column(Float)
    available_at = Column(DateTime)

    appointments = relationship('Appointment', secondary='appointmentservicetype', back_populates='service_types', lazy = 'subquery')

    def __init__(self, service_name, approximate_duration, price, available_at):
        self.service_name = service_name
        self.approximate_duration = approximate_duration
        self.price = price
        self.available_at = available_at