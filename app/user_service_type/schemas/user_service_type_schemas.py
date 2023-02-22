from pydantic import BaseModel
from app.user.schemas import UserSchema
from app.service_type.schemas import ServiceTypeSchema

class UserServiceTypeSchema(BaseModel):
    user_id: str
    user: UserSchema
    service_type_id: str
    service_type_id: ServiceTypeSchema


    class Config:
        orm_mode = True


class UserServiceTypeSchemaIn(BaseModel):
    user_id: str
    service_type_id: str
    
    class Config:
        orm_mode = True