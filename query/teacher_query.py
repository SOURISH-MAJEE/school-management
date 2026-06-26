from sqlalchemy.orm import Session
from models.teacher_model import Teacher
from schemas.teacher_schema import TeacherCreate, TeacherUpdate
from auth.auth import hash_password, verify_password

def create_teacher(db: Session, teacher: TeacherCreate):
    # Hash password before saving
    data = teacher.model_dump()
    data["password"] = hash_password(data["password"])

    new_teacher = Teacher(**data)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def get_all_teachers(db: Session):
    return db.query(Teacher).all()

def get_teacher_by_id(db: Session, teacher_id: int):
    return db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id).first()

def get_teacher_by_email(db: Session, email: str):
    return db.query(Teacher).filter(
        Teacher.email == email).first()

def update_teacher(db: Session, teacher_id: int, teacher: TeacherUpdate):
    db_teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id).first()
    if not db_teacher:
        return None
    data = teacher.model_dump(exclude_unset=True)
    # Hash new password if updated
    if "password" in data:
        data["password"] = hash_password(data["password"])
    for key, value in data.items():
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

def login_teacher(db: Session, email: str, password: str):
    teacher = get_teacher_by_email(db, email)
    if not teacher:
        return None
    if not verify_password(password, teacher.password):
        return None
    return teacher