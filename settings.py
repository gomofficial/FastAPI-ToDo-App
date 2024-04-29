from os import environ


RUNTIME_CONTEXT = environ.get('RUNTIME_CONTEXT', None)


if RUNTIME_CONTEXT == 'docker':
    SECRET_KEY:str = environ.get('Secret_Key')
    SQLALCHEMY_DATABASE_URL:str = "postgresql+asyncpg://"+str(environ.get('POSTGRES_USER'))+":"+environ.get('POSTGRES_PASSWORD')+"@db:5432/"+environ.get('POSTGRES_DB')
else:
    SECRET_KEY:str = 'SOME_SECRET_KEY'
    SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./todo.db"


ACCESS_TOKEN_EXPIRE_MINUTES:int = 30
ALGORITHM:str = "HS256"