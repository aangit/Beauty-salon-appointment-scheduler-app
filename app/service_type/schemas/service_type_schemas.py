from datetime import datetime
from pydantic import BaseModel
from pydantic import UUID4
from datetime import time

class ServiceTypeSchema(BaseModel):
    id: UUID4
    service_name: str
    approximate_duration: time
    price: float
    available_at: datetime

    class Config:
        orm_mode = True


class ServiceTypeSchemaIn(BaseModel):
    service_name: str
    approximate_duration: time
    price: float
    available_at: datetime

    class Config:
        orm_mode = True


class UpdateServiceTypeSchemaIn(BaseModel):
    service_name: str | None = None
    approximate_duration: time | None = None
    price: float | None = None
    available_at: datetime | None = None
    
    
    class Config:
        orm_mode = True