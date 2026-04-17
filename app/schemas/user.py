
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name:str = Field(default="임진우")
    email: str = Field(default="wlsdn@naver.com")
    password: str = Field(default="1234")
    gender: str = Field(default="MALE")
    age: int = Field(default="26")