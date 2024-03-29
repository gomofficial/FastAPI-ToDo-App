from fastapi import FastAPI
from account.routers import auth_router


app = FastAPI()



app.include_router(auth_router, prefix='/account', tags=['account'])


