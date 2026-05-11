from fastapi import APIRouter, Depends, HTTPException

from app.db.models.subtask import SubTask
from app.db.session import AsyncSession, get_db
from app.dependencies.auth import get_current_user
from app.schemas.subtask import SubtaskCreate
from app.services import subtask_service


router = APIRouter()


@router.post("/subtasks")
async def create_subtask(
    subtask: SubtaskCreate,
    db: AsyncSession = Depends(get_db),
    user_id: int = Depends(get_current_user),
):
    new_subtask = SubTask(**subtask.dict())
    result = await subtask_service.create_subtask(db, new_subtask, user_id)

    if result["status"] == "success":
        return result["data"]

    raise HTTPException(status_code=400, detail=result.get("message", "서브태스크 생성에 실패하였습니다."))
