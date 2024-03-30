from sqlalchemy.ext.asyncio import AsyncSession
from db.models import User

class UsersOperation:
    def __init__(self, db_session:AsyncSession) -> None:
        self.db_session = db_session

    async def create(self,username:str,email:str,password:str):
        user = User(username=username, email=email, password=password)

        async with self.db_session as session:
            session.add(user)

        return user