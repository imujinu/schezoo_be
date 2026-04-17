

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from app.db.base import BaseModel


class Schedule(BaseModel):
    __tablename__ = "schedules"
    
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    is_completed = Column(Boolean, default=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)