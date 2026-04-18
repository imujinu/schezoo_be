from fastapi import FastAPI
from app.api.vi import user
app = FastAPI()

app.include_router(user.router)
