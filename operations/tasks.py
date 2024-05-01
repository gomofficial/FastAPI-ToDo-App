from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Task,Category,User
from exceptions import TaskDoesntExists,TaskAlreadyExists,CategoryDoesntExists
import sqlalchemy as sa
from schema.output import TaskOutput
from sqlalchemy.exc import IntegrityError
from utils.jwt import JWTHandler
from uuid import UUID

class TaskOperation:
    def __init__(self, db_session:AsyncSession) -> None:
        self.db_session = db_session

    async def create(self, username:UUID, name:str, description:str, category_id:UUID,):
        user_query     = sa.select(User).where(User.username==username)
        category_query = sa.select(Category).where(Category.id==category_id)

        async with self.db_session as session:
            user_data = await session.scalar(user_query)
            cat_data  = await session.scalar(category_query)
            if cat_data is None:
                raise CategoryDoesntExists
            task = Task()
            task.user_id = user_data.id
            task.name=name
            task.user=user_data
            task.description=description
            task.cat_id=cat_data.id
            task.category=cat_data
            
            # try:
            session.add(task)
            await session.commit()
            # except IntegrityError:
            #     raise TaskAlreadyExists

            return task
    
    async def retrieve(self, username:str, ):
        user_query  = sa.select(User).where(User.username == username)
        async with self.db_session as session:
            user = await session.scalar(user_query)
            query = sa.select(Task).where(Task.user_id == user.id)
            tasks = await session.scalars(query)

            return tasks

    async def update(self, id:UUID, new_name:str, new_description:str, new_cat_id:str):
        query = sa.select(Task).where(Task.id == id)
        cat_query = sa.select(Category).where(Category.id==id)
        async with self.db_session as session:
            task = await session.scalar(query)
            if task is None:
                raise TaskDoesntExists
            cat = await session.scalar(cat_query)
            if cat is None:
                raise CategoryDoesntExists
            update_query =sa.update(Task).where(Task.id == id).values(name=new_name,
                                               description=new_description,
                                                cat_id=cat.id
                                                category=cat)
            task.name = new_name
            await session.execute(update_query)
            await session.commit()
            task.name = new_name

            return task               

    async def delete(self, id:UUID, ):
        query = sa.select(Task).where(Task.id == id)
        delete_query =sa.delete(Task).where(Task.id == id)
        async with self.db_session as session:
            task = await session.scalar(query)
            if task is None:
                raise TaskDoesntExists

            await session.execute(delete_query)
            await session.commit()

            return task

