from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Task,Category,User
from exceptions import UserNotFoundError, UserAlreadyExists, UserAuthenticationError, CategoryAlreadyExists, CategoryDoesntExists
import sqlalchemy as sa
from schema.output import RegisterOutput
from sqlalchemy.exc import IntegrityError
from utils.jwt import JWTHandler
from uuid import UUID

class CategoryOperation:
    def __init__(self, db_session:AsyncSession) -> None:
        self.db_session = db_session

    async def create(self,name:str, username:str, ):
        user_query = sa.select(User).where(User.username==username)

        async with self.db_session as session:
            user_data = await session.scalar(user_query)
            cat = Category()
            cat.user_id=user_data.id
            cat.name=name
            cat.user=user_data
            
            try:
                session.add(cat)
                await session.commit()
            except IntegrityError:
                raise CategoryAlreadyExists

            return cat
    
    async def retrieve(self, username:str, ):
        user_query  = sa.select(User).where(User.username == username)
        async with self.db_session as session:
            user = await session.scalar(user_query)
            query = sa.select(Category).where(Category.user_id == user.id)
            cats = await session.scalars(query)

            return cats

    async def update(self, id:UUID, new_name:str, ):
        query = sa.select(Category).where(Category.id == id)
        update_query =sa.update(Category).where(Category.id == id).values(name=new_name)

        async with self.db_session as session:
            cat = await session.scalar(query)
            if cat is None:
                raise CategoryDoesntExists
            cat.name = new_name

            await session.execute(update_query)
            await session.commit()

            cat.name = new_name

            return cat

    async def delete(self, id:UUID, ):
        query = sa.select(Category).where(Category.id == id)
        delete_query =sa.delete(Category).where(Category.id == id)
        async with self.db_session as session:
            cat = await session.scalar(query)
            if cat is None:
                raise CategoryDoesntExists

            await session.execute(delete_query)
            await session.commit()

            return cat

