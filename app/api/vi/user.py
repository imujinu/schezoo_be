from app.config.security import hash_password
from app.services.user_service import find_user
from fastapi import APIRouter, Depends

from app.db.models.user import User
from app.db.session import AsyncSession, get_db
from app.schemas.user import UserCreate


router = APIRouter()

@router.post("/users")
async def create_user(user : UserCreate , db : AsyncSession = Depends(get_db)):
    new_user = User(
        name = user.name,
        email = user.email,
        password = hash_password(user.password),
        gender = user.gender,
        age=user.age        
    )
    
    db.add(new_user)
    await db.commit()
    
    return {"message" : "user created"}

# @router.get("/users")
# async def get_user(email: str, db: AsyncSessionLocal = Depends(get_db)):
#     user = await find_user(db, email)
#     return user

@router.get("/user")
async def get_user(email : str , db : AsyncSession = Depends(get_db)):
    user = await find_user(db, email)

    return user