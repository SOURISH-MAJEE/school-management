from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class StudentCreate(BaseModel):
    name: str
    email: str
    phone: str

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class StudentResponse(BaseModel):
    student_id: int
    name: str
    email: str
    phone: str
    created_at: Optional[datetime] = None

    model_config = {"from_attributes": True}