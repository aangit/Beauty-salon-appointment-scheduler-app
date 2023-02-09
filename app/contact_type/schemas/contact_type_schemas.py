from pydantic import BaseModel
from pydantic import UUID4


class ContactTypeSchema(BaseModel):
    id: UUID4
    contact_type: str

    class Config:
        orm_mode = True


class ContactTypeSchemaIn(BaseModel):
    contact_type: str

    class Config:
        orm_mode = True