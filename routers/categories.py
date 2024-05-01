from  fastapi import APIRouter, Body, Depends
from  schema._input import *
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from operations.categories import CategoryOperation
from schema import jwt
from schema._input import CategoryInput
from schema.output import CategoryOutput
from utils.auth import JWTHandler
from typing import List


category_router = APIRouter()


@category_router.post("/")
async def create(db_session: Annotated[AsyncSession, Depends(get_db)],
                    data: CategoryInput = Body(),
                    token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):

    category = await CategoryOperation(db_session).create(
        data.name,
        token_data.username,
        )
    
    return category

@category_router.get("/", response_model=List[CategoryOutput])
async def get_categories(db_session: Annotated[AsyncSession, Depends(get_db)],
                    token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):

    category = await CategoryOperation(db_session).retrieve(
        token_data.username,
        )

    return category


@category_router.put("/", response_model=CategoryOutput)
async def update_categories(db_session: Annotated[AsyncSession, Depends(get_db)],
                    data: CategoryUpdate = Body(),
                    token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):

    category = await CategoryOperation(db_session).update(
        data.id,
        data.new_name
        )

    return category


@category_router.delete("/", response_model=CategoryOutput)
async def update_categories(db_session: Annotated[AsyncSession, Depends(get_db)],
                    cat_id: UUID,
                    token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):
    
    category = await CategoryOperation(db_session).delete(cat_id,)

    return category