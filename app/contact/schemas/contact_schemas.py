from pydantic import BaseModel
from pydantic import UUID4
# from app import contact_type
from app.contact_type.schemas import ContactTypeSchema
from app.user.schemas import UserSchema

class ContactSchema(BaseModel):
    id: UUID4
    contact_title: str
    user_id: str
    user: UserSchema
    contact_type_id: str
    contact_type: ContactTypeSchema

    class Config:
        orm_mode = True


class ContactSchemaIn(BaseModel):
    contact_title: str
    user_id: str
    contact_type_id: str
    
    class Config:
        orm_mode = True