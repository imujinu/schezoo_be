from fastapi import APIRouter, Depends

from app.db.models.schedule import Schedule
from app.db.session import get_db, AsyncSession
from app.dependencies.auth import get_current_user
from app.schemas.schedule import ScheduleCreate


router = APIRouter()

@router.post("/schedules")
async def create_schedule(schedule : ScheduleCreate, 
                          user_id: int = Depends(get_current_user), 
                          db : AsyncSession = Depends(get_db)):
    
    new_schedule = Schedule(
        **schedule.dict(),
        user_id = user_id
    )
    return {"message" : "schedule created"}


