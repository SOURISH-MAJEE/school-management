from sqlalchemy.orm import Session
from models.student_model import Student
from schemas.student_schema import StudentCreate, StudentUpdate
from auth.auth import hash_password, verify_password

def create_student(db: Session, student: StudentCreate):
    # Hash password before saving
    data = student.model_dump()
    data["password"] = hash_password(data["password"])

    new_student = Student(**data)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_all_students(db: Session):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(
        Student.student_id == student_id).first()

def get_student_by_roll(db: Session, roll_number: str):
    return db.query(Student).filter(
        Student.roll_number == roll_number).first()

def get_students_by_class(db: Session, class_id: int):
    return db.query(Student).filter(
        Student.class_id == class_id).all()

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = db.query(Student).filter(
        Student.student_id == student_id).first()
    if not db_student:
        return None
    data = student.model_dump(exclude_unset=True)
    # Hash new password if updated
    if "password" in data:
        data["password"] = hash_password(data["password"])
    for key, value in data.items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(
        Student.student_id == student_id).first()
    if not db_student:
        return None
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}

def login_student(db: Session, roll_number: str, password: str):
    student = get_student_by_roll(db, roll_number)
    if not student:
        return None
    if not verify_password(password, student.password):
        return None
    return student