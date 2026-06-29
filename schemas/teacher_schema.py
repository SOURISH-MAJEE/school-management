from pydantic import BaseModel
from typing import Optional

class TeacherCreate(BaseModel):
    name     : str
    age      : int
    gender   : str
    email    : str
    phone    : str
    password : str  

class TeacherUpdate(BaseModel):
    name     : Optional[str] = None
    age      : Optional[int] = None
    gender   : Optional[str] = None
    email    : Optional[str] = None
    phone    : Optional[str] = None
    password : Optional[str] = None

class TeacherResponse(BaseModel):
    teacher_id : int
    name       : str
    age        : int
    gender     : str
    email      : str
    phone      : str
    

    model_config = {"from_attributes": True}