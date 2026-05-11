from fastapi import FastAPI
from app.api.v1 import user, schedule, auth, subtask
app = FastAPI(
    swagger_ui_parameters={
        "persistAuthorization": True  # 로컬스토리지에 토큰 정보 저장
    })

app.include_router(user.router)
app.include_router(schedule.router)
app.include_router(auth.router)
app.include_router(subtask.router)
