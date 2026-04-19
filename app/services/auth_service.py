from os import error

from app.config.security import create_access_token, verify_password
from app.repositories.user_repository import find_user_by_email


async def login_user(db, email : str, password : str):
    user = await find_user_by_email(db, email)

    if not user :
        return None
    
    if not verify_password(password, user.password):
        return None
    
    token = create_access_token({"user_id" : user.id})

    return token