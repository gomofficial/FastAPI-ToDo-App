from os import environ as env



SECRET_KEY:str = env['MY_VARIABLE']
ACCESS_TOKEN_EXPIRE_MINUTES:int = 30
ALGORITHM:str = "HS256"