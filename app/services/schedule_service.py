
from app.repositories import schedule_repository

async def create_schedule(db, schedule):
    result = await schedule_repository.create_schedule(db, schedule)
    return result


async def get_user_schedules(db, user_id):
    schedules = await schedule_repository.find_schedules_by_userId(db,user_id)
    return schedules
