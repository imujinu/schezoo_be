
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.db.base import BaseModel


class SubTask(BaseModel):
    __tablename__ = "subtask"
    
    schedule_id = Column(Integer , ForeignKey("schedules.id"))
    content = Column(String)
    is_completed = Column(Boolean, default=False)