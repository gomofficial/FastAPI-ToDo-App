from pydantic import BaseModel


class RegisterInput(BaseModel):
    username:str
    email:str
    password:str
    is_staff:bool
    is_active:bool
