from pydantic import BaseModel


class SubtaskCreate(BaseModel):
    schedule_id: int
    content: str = "테스트 서브태스크"
    is_completed: bool = False 