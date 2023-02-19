from pydantic import BaseModel
from pydantic import UUID4


class StatusSchema(BaseModel):
    id: UUID4
    status: str

    class Config:
        orm_mode = True


class StatusSchemaIn(BaseModel):
    status: str

    class Config:
        orm_mode = True