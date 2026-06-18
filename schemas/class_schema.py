from pydantic import BaseModel
from typing import Optional

class ClassCreate(BaseModel):
    class_name: str
    section   : str

class ClassUpdate(BaseModel):
    class_name: Optional[str] = None
    section   : Optional[str] = None

class ClassResponse(BaseModel):
    class_id  : int
    class_name: str
    section   : str

    model_config = {"from_attributes": True}