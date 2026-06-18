from pydantic import BaseModel
from typing import Optional

class SubjectCreate(BaseModel):
    subject_name: str

class SubjectUpdate(BaseModel):
    subject_name: Optional[str] = None

class SubjectResponse(BaseModel):
    subject_id  : int
    subject_name: str

    model_config = {"from_attributes": True}