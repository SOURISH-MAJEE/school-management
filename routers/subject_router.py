from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.subject_schema import SubjectCreate, SubjectUpdate, SubjectResponse
from query import subject_query

router = APIRouter(prefix="/subjects", tags=["Subjects"])

@router.post("/", response_model=SubjectResponse)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return subject_query.create_subject(db, subject)

@router.get("/", response_model=list[SubjectResponse])
def get_subjects(db: Session = Depends(get_db)):
    return subject_query.get_all_subjects(db)

@router.get("/{subject_id}", response_model=SubjectResponse)
def get_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = subject_query.get_subject_by_id(db, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject

@router.get("/teacher/{teacher_id}", response_model=list[SubjectResponse])
def get_subjects_by_teacher(teacher_id: int, db: Session = Depends(get_db)):
    return subject_query.get_subjects_by_teacher(db, teacher_id)

@router.put("/{subject_id}", response_model=SubjectResponse)
def update_subject(subject_id: int, subject: SubjectUpdate,
                   db: Session = Depends(get_db)):
    updated = subject_query.update_subject(db, subject_id, subject)
    if not updated:
        raise HTTPException(status_code=404, detail="Subject not found")
    return updated

@router.delete("/{subject_id}")
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    result = subject_query.delete_subject(db, subject_id)
    if not result:
        raise HTTPException(status_code=404, detail="Subject not found")
    return result