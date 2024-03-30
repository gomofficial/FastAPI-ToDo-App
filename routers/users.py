from  fastapi import APIRouter, Body, Depends
from  schema._input import RegisterInput
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from operations.users import UsersOperation

auth_router = APIRouter()


@auth_router.post('/register')
async def register( db_session: Annotated[AsyncSession, Depends(get_db)],
                    data:RegisterInput = Body()):
    
    user = await UsersOperation(db_session).create(
        data.username,
        data.email,
        data.password
        )


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

