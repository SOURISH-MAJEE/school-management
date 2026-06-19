from pydantic import BaseModel
from typing import Optional
from datetime import date

class AttendanceSessionCreate(BaseModel):
    class_id   : int
    subject_id : int
    teacher_id : int
    date       : date
    period     : int

class AttendanceSessionUpdate(BaseModel):
    class_id   : Optional[int] = None
    subject_id : Optional[int] = None
    teacher_id : Optional[int] = None
    date       : Optional[date] = None
    period     : Optional[int] = None

class AttendanceSessionResponse(BaseModel):
    session_id : int
    class_id   : int
    subject_id : int
    teacher_id : int
    date       : date
    period     : int

    model_config = {"from_attributes": True}