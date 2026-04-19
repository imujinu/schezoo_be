from fastapi import FastAPI
from app.api.vi import user, schedule, auth
app = FastAPI()

app.include_router(user.router)
app.include_router(schedule.router)
app.include_router(auth.router)
