from pydantic import BaseModel


class RegisterInput(BaseModel):
    username:str
    email:str
    password:str

class UpdateUserProfile(BaseModel):
    new_username:str

class AuthenticateUser(BaseModel):
    username:str
    password:str
