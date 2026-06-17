from pydantic import BaseModel
from typing import Optional, List

class TeacherCreate(BaseModel):
    name: str
    email: str
    phone: str

class TeacherUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class TeacherResponse(BaseModel):
    teacher_id: int
    name: str
    email: str
    phone: str

    model_config = {"from_attributes": True}