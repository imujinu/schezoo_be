# app/repository/user_repository.py

# from sqlalchemy import select
# from app.db.models.user import User

# async def get_user_by_email(db, email: str):
#     result = await db.execute(
#         select(User).where(User.email == email)
#     )
#     return result.scalars().first()

from sqlalchemy import select
from app.db.models.user import User

async def find_user_by_email(db, email: str):
    result = await db.execute(
        select(User).where(User.email == email)
    )

    return result.scalars().first()