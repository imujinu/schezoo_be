from fastapi import APIRouter, Depends

from app.db.models.user import User
from app.db.session import AsyncSessionLocal, get_db
from app.schemas.user import UserCreate


router = APIRouter()

@router.post("/users")
async def create_user(user : UserCreate , db : AsyncSessionLocal = Depends(get_db)):
    new_user = User(
        name = user.name,
        email = user.email,
        password = user.password,
        gender = user.gender,
        age=user.age        
    )
    
    db.add(new_user)
    await db.commit()
    
    return {"message" : "user created"}

@router.get("/users")
async def get_user(email: str, db: AsyncSessionLocal = Depends(get_db)):
    user = await find_user(db, email)
    return user