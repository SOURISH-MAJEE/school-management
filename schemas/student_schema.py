from pydantic import BaseModel
from typing import Optional

class StudentCreate(BaseModel):
    roll_number : str
    name        : str
    age         : int
    gender      : str
    phone       : Optional[str] = None
    class_id    : int
    password    : str  # plain password from user

class StudentUpdate(BaseModel):
    roll_number : Optional[str] = None
    name        : Optional[str] = None
    age         : Optional[int] = None
    gender      : Optional[str] = None
    phone       : Optional[str] = None
    class_id    : Optional[int] = None
    password    : Optional[str] = None

class StudentResponse(BaseModel):
    student_id  : int
    roll_number : str
    name        : str
    age         : int
    gender      : str
    phone       : Optional[str] = None
    class_id    : int
    # NOTE: password NOT included in response for security!

    model_config = {"from_attributes": True}