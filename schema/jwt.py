from pydantic import BaseModel

class JWTPayload(BaseModel):
    username:str
    exp:int


class JWTResponsePayload(BaseModel):
    access: str
