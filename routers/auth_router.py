from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.auth_schema import TeacherLogin, StudentLogin, LoginResponse
from query.teacher_query import login_teacher
from query.student_query import login_student

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/teacher-login", response_model=LoginResponse)
def teacher_login(data: TeacherLogin, db: Session = Depends(get_db)):
    teacher = login_teacher(db, data.email, data.password)
    if not teacher:
        raise HTTPException(
            status_code=401,
            detail="Wrong email or password!"
        )
    return {
        "message"   : "Login successful!",
        "user_type" : "teacher",
        "user_id"   : teacher.teacher_id,
        "name"      : teacher.name
    }

@router.post("/student-login", response_model=LoginResponse)
def student_login(data: StudentLogin, db: Session = Depends(get_db)):
    student = login_student(db, data.roll_number, data.password)
    if not student:
        raise HTTPException(
            status_code=401,
            detail="Wrong roll number or password!"
        )
    return {
        "message"   : "Login successful!",
        "user_type" : "student",
        "user_id"   : student.student_id,
        "name"      : student.name
    }