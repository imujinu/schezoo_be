from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base
from app.db.models import user, schedule, subtask

app = FastAPI()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def on_startup():
    await init_db()