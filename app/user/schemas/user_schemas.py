from pydantic import BaseModel
from pydantic import UUID4
from pydantic import EmailStr
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