from pydantic import BaseModel
from typing import Optional

class AttendanceCreate(BaseModel):
    session_id: int
    student_id: int
    status    : str

class AttendanceUpdate(BaseModel):
    status: Optional[str] = None

class AttendanceResponse(BaseModel):
    attendance_id: int
    session_id   : int
    student_id   : int
    status       : str

    model_config = {"from_attributes": True}