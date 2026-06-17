from sqlalchemy.orm import Session
from models.student_model import Student
from schemas.student_schema import StudentCreate, StudentUpdate

def create_student(db: Session, student: StudentCreate):
    new_student = Student(**student.model_dump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

def get_all_students(db: Session):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.student_id == student_id).first()

def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if not db_student:
        return None
    for key, value in student.model_dump(exclude_unset=True).items():
        setattr(db_student, key, value)
    db.commit()
    db.refresh(db_student)
    return db_student

def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if not db_student:
        return None
    db.delete(db_student)
    db.commit()
    return {"message": "Student deleted successfully"}