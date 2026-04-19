from pydantic import BaseModel, Field
from datetime import datetime, timezone


def get_today_midnight():
    now = datetime.now(timezone.utc)
    return now.replace(hour=23, minute=59, second=59, microsecond=0)


class ScheduleCreate(BaseModel):
    title: str = "테스트 일정"
    contents: str = "테스트 내용"
    start_time: datetime = Field(default_factory=datetime.now(timezone.utc))
    end_time: datetime = Field(default_factory=get_today_midnight)
