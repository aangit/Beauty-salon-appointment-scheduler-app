from typing import List
from pydantic import BaseModel
from pydantic import UUID4
from pydantic import EmailStr

from app.service_type.schemas.service_type_schemas import ServiceTypeSchema
from app.user_type.schemas import UserTypeSchema

class UserSchema(BaseModel):
    id: UUID4
    email: str
    # password: str
    user_type_id: str
    user_type: UserTypeSchema
    
    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    email: EmailStr
    password: str
    user_type_id: str
    
    class Config:
        orm_mode = True



class UserLoginShema(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class UserLoginShemaIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True

class EmployeeSchema(BaseModel):
    id: UUID4
    email: str
    # password: str
    user_type_id: str
    user_type: UserTypeSchema
    service_types: List[ServiceTypeSchema]
    # days_of_week: List[DayOfWeekSchema]

    class Config:
        orm_mode = True

class EmployeeSchemaIn(BaseModel):
    email: EmailStr
    password: str
    # user_type_id: str
    service_types: List[str]
    # days_of_week: List[str]

    class Config:
        orm_mode = True

class UpdateEmployeeSchemaIn(BaseModel):
    # email: EmailStr | None = None
    # password: str | None = None
    service_types: List[str] | None = None
