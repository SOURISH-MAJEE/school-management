from pydantic import BaseModel

class TeacherLogin(BaseModel):
    email    : str
    password : str

class StudentLogin(BaseModel):
    roll_number : str
    password    : str

class LoginResponse(BaseModel):
    message    : str
    user_type  : str  
    user_id    : int
    name       : str