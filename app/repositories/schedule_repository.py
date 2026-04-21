

from sqlalchemy import select

from app.db.models.schedule import Schedule


async def create_schedule(db, schedule : Schedule):
    try:
        db.add(schedule)
        await db.commit()
        await db.refresh(schedule)

        return {"status" : "success", "data" : schedule}
    except Exception as e:
        await db.rollback()
        print(f"에러발생 : {e}")
        return {"status" : "fail", "message" : e}


async def find_schedules_by_userId(db, userId : int):
    result = await db.execute(
        select(Schedule).where(Schedule.user_id == userId)
    )

    return result.scalars().all()


