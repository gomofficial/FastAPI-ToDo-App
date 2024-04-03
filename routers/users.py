from  fastapi import APIRouter, Body, Depends
from  schema._input import *
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from operations.users import UsersOperation

auth_router = APIRouter()


@auth_router.post('/register')
async def register( db_session: Annotated[AsyncSession, Depends(get_db)],
                    data: RegisterInput = Body()):
    
    user = await UsersOperation(db_session).create(
        data.username,
        data.email,
        data.password
        )
    
    return user


@auth_router.post("/login")
async def login():
    ...

@auth_router.get("/{username}")
async def get_user_profile(db_session: Annotated[AsyncSession, Depends(get_db)],
                           username: str):
    uesr_profile = await UsersOperation(db_session).get_user_by_username(username)

    return uesr_profile


@auth_router.put("/")
async def update_user_profile(db_session: Annotated[AsyncSession, Depends(get_db)],
                              data:UpdateUserProfile = Body()):
    user = await UsersOperation(db_session).update_username(
        data.old_username,data.new_username)

    return user

@auth_router.delete("/")
async def user_delete_account(db_session: Annotated[AsyncSession, Depends(get_db)],
                              data:DeleteUserProfile = Body()):
    await UsersOperation(db_session).user_delete_account(
        data.username, data.password)
