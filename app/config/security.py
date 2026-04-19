from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from app.config.core import SECRET_KEY, ALGORITHM

pwd_context = CryptContext(schemes=["argon2" , "bcrypt"], deprecated="auto")


# 🔹 비밀번호 검증
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


# 🔹 비밀번호 해싱
def hash_password(password):
    return pwd_context.hash(password)


# 🔹 토큰 생성
def create_access_token(data: dict, expires_delta: int = 60):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
