from  fastapi import APIRouter, Body, Depends
from  schema._input import *
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from operations.users import UsersOperation
from schema import jwt
from utils.jwt import JWTHandler

category_router = APIRouter()


@category_router.post("/")
async def create():
    ...