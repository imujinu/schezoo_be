
from sqlalchemy import Column, Enum, Integer, String

from app.db.base import BaseModel
from app.db.models.genderEnum import GenderEnum


class User(BaseModel):
    __tablename__="users"
    
    name = Column(String)
    password = Column(String)
    email = Column(String, unique=True)
    gender = Column(Enum(GenderEnum))
    age = Column(Integer)
    gender = Column(Enum(GenderEnum))
    