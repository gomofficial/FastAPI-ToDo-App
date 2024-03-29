from  fastapi import APIRouter, Body
from  schema._input import RegisterInput

auth_router = APIRouter()


@auth_router.post('/register')
async def register(data:RegisterInput = Body()):
    return data


@auth_router.post("/login")
async def login():
    ...

@auth_router.get("/")
async def get_user_profile():
    ...

@auth_router.put("/")
async def update_user_profile():
    ...

