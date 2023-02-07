from pydantic import BaseModel
from pydantic import UUID4


class UserTypeSchema(BaseModel):
    id: UUID4
    user_type: str

    class Config:
        orm_mode = True


class UserTypeSchemaIn(BaseModel):
    user_type: str

    class Config:
        orm_mode = True