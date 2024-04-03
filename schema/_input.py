from pydantic import BaseModel


class RegisterInput(BaseModel):
    username:str
    email:str
    password:str

class UpdateUserProfile(BaseModel):
    old_username:str
    new_username:str

class DeleteUserProfile(BaseModel):
    username:str
    password:str