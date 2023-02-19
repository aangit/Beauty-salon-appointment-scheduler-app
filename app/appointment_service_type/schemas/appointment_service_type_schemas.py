from pydantic import BaseModel
# from pydantic import UUID4
from app.appointment.schemas import AppointmentSchema
from app.service_type.schemas import ServiceTypeSchema

class AppointmentServiceTypeSchema(BaseModel):
    appointment_id: str
    appointment_id: AppointmentSchema
    service_type_id: str
    service_type_id: ServiceTypeSchema


    class Config:
        orm_mode = True


class AppointmentServiceTypeSchemaIn(BaseModel):
    appointment_id: str
    service_type_id: str
    
    class Config:
        orm_mode = True