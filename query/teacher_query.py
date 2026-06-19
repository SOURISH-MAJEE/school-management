from sqlalchemy.orm import Session
from models.teacher_model import Teacher
from schemas.teacher_schema import TeacherCreate, TeacherUpdate

def create_teacher(db: Session, teacher: TeacherCreate):
    new_teacher = Teacher(**teacher.model_dump())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_all_teachers(db: Session):
    return db.query(Teacher).all()

def get_teacher_by_id(db: Session, teacher_id: int):
    return db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id).first()

def update_teacher(db: Session, teacher_id: int, teacher: TeacherUpdate):
    db_teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id).first()
    if not db_teacher:
        return None
    for key, value in teacher.model_dump(exclude_unset=True).items():
        setattr(db_teacher, key, value)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def delete_teacher(db: Session, teacher_id: int):
    db_teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id).first()
    if not db_teacher:
        return None
    db.delete(db_teacher)
    db.commit()
    return {"message": "Teacher deleted successfully"}