from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class RegisterInput(BaseModel):
    username:str
    email:str
    password:str

class UpdateUserProfile(BaseModel):
    new_username:str

class AuthenticateUser(BaseModel):
    username:str
    password:str



class CategoryInput(BaseModel):
    name:str

class CategoryUpdate(BaseModel):
    id:UUID
    new_name:str


class TaskInput(BaseModel):
    name:str
    description:str
    category_id:UUID


class TaskUpdate(BaseModel):
    new_name:Optional[str] = None
    new_description:Optional[str] = None
    new_cat_id: Optional[UUID] = None