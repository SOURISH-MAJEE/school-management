from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.student_schema import StudentCreate, StudentUpdate, StudentResponse
from query import student_query

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return student_query.create_student(db, student)

@router.get("/", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return student_query.get_all_students(db)

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = student_query.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/class/{class_id}", response_model=list[StudentResponse])
def get_students_by_class(class_id: int, db: Session = Depends(get_db)):
    return student_query.get_students_by_class(db, class_id)

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentUpdate,
                   db: Session = Depends(get_db)):
    updated = student_query.update_student(db, student_id, student)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    result = student_query.delete_student(db, student_id)
    if not result:
        raise HTTPException(status_code=404, detail="Student not found")
    return result