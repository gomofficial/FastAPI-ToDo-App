from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./todo.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = async_sessionmaker(bind=engine,
                            autocommmit=False,
                            autoflush=False,
                            )

class Base(DeclarativeBase, MappedAsDataclass):
    pass

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        await db.close()

