from pydantic import BaseModel
from typing import Optional

class SubjectCreate(BaseModel):
    subject_name : str
    teacher_id   : Optional[int] = None

class SubjectUpdate(BaseModel):
    subject_name : Optional[str] = None
    teacher_id   : Optional[int] = None

class SubjectResponse(BaseModel):
    subject_id   : int
    subject_name : str
    teacher_id   : Optional[int] = None

    model_config = {"from_attributes": True}