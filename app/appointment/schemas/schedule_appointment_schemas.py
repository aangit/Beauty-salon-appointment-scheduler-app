from datetime import datetime
from pydantic import BaseModel
from pydantic import UUID4
from app.user.schemas import UserSchema
from app.status.schemas import StatusSchema
from datetime import datetime

class ScheduleAppointmentSchema(BaseModel):
    id: UUID4
    appointment_datetime: datetime
    user_id: str
    status_id: str
    user: UserSchema
    status: StatusSchema
    

    class Config:
        orm_mode = True


class ScheduleAppointmentSchemaIn(BaseModel):
    appointment_datetime: datetime
    user_id: str
    status_id: str
    
    
    class Config:
        orm_mode = True