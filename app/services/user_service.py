
from app.repository.user_repository import get_user_by_email

async def find_user(db, email: str):
    return await get_user_by_email(db, email)