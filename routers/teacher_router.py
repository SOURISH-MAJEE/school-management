from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.teacher_schema import TeacherCreate, TeacherUpdate, TeacherResponse
from query import teacher_query

router = APIRouter(prefix="/teachers", tags=["Teachers"])

@router.post("/", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return teacher_query.create_teacher(db, teacher)

@router.get("/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    return teacher_query.get_all_teachers(db)

@router.get("/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = teacher_query.get_teacher_by_id(db, teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@router.put("/{teacher_id}", response_model=TeacherResponse)
def update_teacher(teacher_id: int, teacher: TeacherUpdate,
                   db: Session = Depends(get_db)):
    updated = teacher_query.update_teacher(db, teacher_id, teacher)
    if not updated:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return updated

@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    result = teacher_query.delete_teacher(db, teacher_id)
    if not result:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return result