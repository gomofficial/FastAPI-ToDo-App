from sqlalchemy.ext.asyncio import AsyncSession
from db.models import Task,Category
from exceptions import UserNotFoundError, UserAlreadyExists, UserAuthenticationError
import sqlalchemy as sa
from schema.output import RegisterOutput
from sqlalchemy.exc import IntegrityError
from utils.auth import JWTHandler

# class CategoryOperation:
#     def __init__(self, db_session:AsyncSession) -> None:
#         self.db_session = db_session

#     async def create(self,name:str, user_id:int, ):
#         cat = Category()

#         async with self.db_session as session:
#             try:
#                 session.add(cat)
#                 await session.commit()
#             except IntegrityError:
#                 raise UserAlreadyExists

#         return cat