from pydantic import BaseModel
from uuid import UUID

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
    ...