from sqlalchemy.orm import Session
from models.subject_model import Subject
from schemas.subject_schema import SubjectCreate, SubjectUpdate

def create_subject(db: Session, subject: SubjectCreate):
    new_subject = Subject(**subject.model_dump())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject

def get_all_subjects(db: Session):
    return db.query(Subject).all()

def get_subject_by_id(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.subject_id == subject_id).first()

def update_subject(db: Session, subject_id: int, subject: SubjectUpdate):
    db_subject = db.query(Subject).filter(Subject.subject_id == subject_id).first()
    if not db_subject:
        return None
    for key, value in subject.model_dump(exclude_unset=True).items():
        setattr(db_subject, key, value)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def delete_subject(db: Session, subject_id: int):
    db_subject = db.query(Subject).filter(Subject.subject_id == subject_id).first()
    if not db_subject:
        return None
    db.delete(db_subject)
    db.commit()
    return {"message": "Subject deleted successfully"}