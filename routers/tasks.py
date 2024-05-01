from  fastapi import APIRouter, Body, Depends
from  schema._input import *
from db.engine import get_db
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from operations.tasks import TaskOperation
from schema import jwt
<<<<<<< HEAD
from schema._input import TaskInput
from schema.output import TaskOutput
from utils.jwt import JWTHandler
from typing import List, Optional

=======
from utils.auth import JWTHandler
>>>>>>> 5205ac8fbdda6834173f48e97189dbbb07857b4a

task_router = APIRouter()


@task_router.post("/")
async def create(db_session: Annotated[AsyncSession, Depends(get_db)],
                    data: TaskInput = Body(),
                    token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):

    task = await TaskOperation(db_session).create(
        token_data.username,
        data.name,
        data.description,
        data.category_id,
        )
    
    return task


# @task_router.get("/", response_model=List[TaskOutput])
# async def get_categories(db_session: Annotated[AsyncSession, Depends(get_db)],
#                     token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):

#     tasks = await TaskOperation(db_session).retrieve(
#         token_data.username,
#         )

#     return tasks


# @task_router.get("/{cat_name}/", response_model=List[TaskOutput])
# async def get_categories(db_session: Annotated[AsyncSession, Depends(get_db)],
#                     cat_name:str,task_id: Optional[str] = None,
#                     token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):

#     tasks = await TaskOperation(db_session).retrieve(
#         token_data.username,
#         cat_name,
#         task_id,
#         )

#     return tasks


# @task_router.put("/", response_model=TaskOutput)
# async def update_categories(db_session: Annotated[AsyncSession, Depends(get_db)],
#                     task_id:UUID,
#                     data: TaskUpdate = Body(),
#                     token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):

#     task = await TaskOperation(db_session).update(
#             token_data.username,
#             task_id,
#             data.new_name,
#             data.new_description,
#             data.new_cat_id,
#         )

#     return task


# @task_router.delete("/", response_model=TaskOutput)
# async def update_categories(db_session: Annotated[AsyncSession, Depends(get_db)],
#                     task_id:UUID,
#                     token_data:jwt.JWTPayload = Depends(JWTHandler.verify_token)):
    
#     task = await TaskOperation(db_session).delete(token_data.username, task_id,)

#     return task