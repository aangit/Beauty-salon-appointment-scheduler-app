from pydantic import BaseModel
from pydantic import UUID4
from app import user_type
from app.user_type.schemas import UserTypeSchema

class UserSchema(BaseModel):
    id: UUID4
    name: str
    user_type_id: str
    user_type: UserTypeSchema

    class Config:
        orm_mode = True


class UserSchemaIn(BaseModel):
    name: str
    user_type_id: str
    
    class Config:
        orm_mode = True