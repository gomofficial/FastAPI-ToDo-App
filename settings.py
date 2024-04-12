from os import environ as env



SECRET_KEY:str = env['Secret_Key']
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://"+str(env['POSTGRES_USER'])+":"+env['POSTGRES_PASSWORD']+"@db:5432/"+env['POSTGRES_DB']
# SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./todo.db"


ACCESS_TOKEN_EXPIRE_MINUTES:int = 30
ALGORITHM:str = "HS256"