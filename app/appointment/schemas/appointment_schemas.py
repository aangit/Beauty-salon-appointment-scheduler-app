from datetime import datetime
from pydantic import BaseModel
from pydantic import UUID4
from app.user.schemas import UserSchema
from app.status.schemas import StatusSchema
from datetime import datetime
from app.service_type.schemas import ServiceTypeSchema
from typing import List

class AppointmentSchema(BaseModel):
    id: UUID4
    appointment_datetime: datetime
    client_id: str
    employee_id: str
    status_id: str
    client: UserSchema
    employee: UserSchema
    status: StatusSchema
    service_types: List[ServiceTypeSchema]

    class Config:
        orm_mode = True


class AppointmentSchemaIn(BaseModel):
    appointment_datetime: datetime
    client_id: str
    employee_id: str
    service_types: List[str]
    
    
    class Config:
        orm_mode = True

class UpdateAppointmentSchemaIn(BaseModel):
    appointment_datetime: datetime | None = None
    client_id: str | None = None
    employee_id: str | None = None
    status_id: str | None = None
    
    
    class Config:
        orm_mode = True