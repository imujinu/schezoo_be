from sqlalchemy import select

from app.db.models.subtask import SubTask


async def create_subtask(db, subtask: SubTask):
    try:
        db.add(subtask)
        await db.commit()
        await db.refresh(subtask)
        return {"status": "success", "data": subtask}
    except Exception as e:
        await db.rollback()
        print(f"에러발생 : {e}")
        return {"status": "fail", "message": str(e)}


async def find_subtasks_by_schedule_id(db, schedule_id: int):
    result = await db.execute(
        select(SubTask).where(SubTask.schedule_id == schedule_id)
    )
    return result.scalars().all()
