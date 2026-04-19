from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.db.session import get_db, AsyncSession
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import login_user


router = APIRouter()

@router.post("/login", response_model=TokenResponse)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db : AsyncSession = Depends(get_db)):
    email = form_data.username  
    password = form_data.password

    token = await login_user(db , email, password)
    
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return {"access_token" : token, "token_type": "bearer"}