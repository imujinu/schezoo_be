from app.repositories import schedule_repository, subtask_repository


async def create_subtask(db, subtask, user_id: int):
    schedule = await schedule_repository.find_schedule_by_id(db, subtask.schedule_id)
    if schedule is None:
        return {"status": "fail", "message": "Schedule not found."}
    if schedule.user_id != user_id:
        return {"status": "fail", "message": "Unauthorized schedule access."}

    return await subtask_repository.create_subtask(db, subtask)


async def get_subtasks_by_schedule(db, schedule_id: int, user_id: int):
    schedule = await schedule_repository.find_schedule_by_id(db, schedule_id)
    if schedule is None or schedule.user_id != user_id:
        return {"status": "fail", "message": "Unauthorized or schedule not found."}

    return await subtask_repository.find_subtasks_by_schedule_id(db, schedule_id)
