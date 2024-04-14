from pydantic import BaseModel
from uuid import UUID

class UserOutput(BaseModel):
    username:str
    email:str
    is_staff:bool
    is_active:bool
    id:UUID

class RegisterOutput(BaseModel):
    username:str
    id: UUID

class CategoryOutput(BaseModel):
    id:UUID
    name:str