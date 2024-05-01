from  fastapi import APIRouter, Body, Depends
from  schema._input import *
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from operations.users import UsersOperation
from schema import jwt
from utils.auth import JWTHandler
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

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


@auth_router.get("/{username}",)
async def get_user_profile(db_session: Annotated[AsyncSession, Depends(get_db)],
                           username: str):
    uesr_profile = await UsersOperation(db_session).get_user_by_username(username)

    return uesr_profile


@auth_router.put("/")
async def update_user_profile(db_session: Annotated[AsyncSession, Depends(get_db)],
                              data:UpdateUserProfile = Body(),
                              token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):
    
    user = await UsersOperation(db_session).update_username(
        token_data.username, data.new_username)

    return user


@auth_router.delete("/")
async def user_delete_account(db_session: Annotated[AsyncSession, Depends(get_db)],
                              token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):
    await UsersOperation(db_session).user_delete_account(token_data.username)


@auth_router.post("/login")
async def authenticate(db_session: Annotated[AsyncSession, Depends(get_db)],
                              form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    token = await UsersOperation(db_session).login(form_data.username,form_data.password)
    return token

