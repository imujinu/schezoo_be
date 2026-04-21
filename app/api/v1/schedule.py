from fastapi import APIRouter, Depends, HTTPException

from app.db.models.schedule import Schedule
from app.db.session import get_db, AsyncSession
from app.dependencies.auth import get_current_user
from app.schemas.schedule import ScheduleCreate
from app.services import schedule_service


router = APIRouter()

@router.post("/schedules")
async def create_schedule(schedule : ScheduleCreate, 
                          user_id: int = Depends(get_current_user), 
                          db : AsyncSession = Depends(get_db)):
    
    new_schedule = Schedule(
        **schedule.dict(),
        user_id = user_id
    )
    new_schedule.start_time = new_schedule.start_time.replace(tzinfo=None)
    new_schedule.end_time = new_schedule.end_time.replace(tzinfo=None)

    result = await schedule_service.create_schedule(db, new_schedule)

    if result["status"] == "success" : 
        return result["data"]
    else:
        raise HTTPException(status_code=400, detail="일정 생성에 실패하였습니다.")

@router.get("/schedule")
async def get_user_schedules(db:AsyncSession=Depends(get_db), user_id : int = Depends(get_current_user)):

    schedules = await schedule_service.get_user_schedules(db, user_id)
    return schedules



