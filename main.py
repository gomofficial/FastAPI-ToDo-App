from fastapi import FastAPI
from routers.users import auth_router
from routers.categories import category_router
from routers.tasks import task_router
from db import engine, Base

app = FastAPI()


@app.on_event("startup")
async def init_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


app.include_router(auth_router, prefix='/account', tags=['account'])
app.include_router(auth_router, prefix='/category', tags=['category'])
app.include_router(auth_router, prefix='/task', tags=['task'])
