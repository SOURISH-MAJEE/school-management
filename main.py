from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Teacher, Student, Subject, Class, Attendance
from datetime import date

app = FastAPI()

# SCHEMAS 

class TeacherSchema(BaseModel):
    name: str
    email: str
    phone: str

class StudentSchema(BaseModel):
    name: str
    email: str
    phone: str

class SubjectSchema(BaseModel):
    subject_name: str
    teacher_id: int

class ClassSchema(BaseModel):
    class_name: str
    subject_id: int

class AttendanceSchema(BaseModel):
    student_id: int
    class_id: int
    date: date
    status: str

# TEACHER ROUTES


@app.post("/teachers/")
def create_teacher(teacher: TeacherSchema, db: Session = Depends(get_db)):
    new_teacher = Teacher(**teacher.dict())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

@app.get("/teachers/")
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()

@app.get("/teachers/{teacher_id}")
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@app.put("/teachers/{teacher_id}")
def update_teacher(teacher_id: int, teacher: TeacherSchema, db: Session = Depends(get_db)):
    db_teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    for key, value in teacher.dict().items():
        setattr(db_teacher, key, value)
    db.commit()
    return db_teacher

@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(teacher)
    db.commit()
    return {"message": "Teacher deleted successfully"}

# STUDENT ROUTES

@app.post("/students/")
def create_student(student: StudentSchema, db: Session = Depends(get_db)):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

@app.get("/students/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}")
def update_student(student_id: int, student: StudentSchema, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.student_id == student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student.dict().items():
        setattr(db_student, key, value)
    db.commit()
    return db_student

@app.delete("/students/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.student_id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}
# ─────────────────────────────────────
# SUBJECT ROUTES
# ─────────────────────────────────────

@app.post("/subjects/")
def create_subject(subject: SubjectSchema, db: Session = Depends(get_db)):
    new_subject = Subject(**subject.dict())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)
    return new_subject

@app.get("/subjects/")
def get_subjects(db: Session = Depends(get_db)):
    return db.query(Subject).all()


# CLASS ROUTES


@app.post("/classes/")
def create_class(cls: ClassSchema, db: Session = Depends(get_db)):
    new_class = Class(**cls.dict())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

@app.get("/classes/")
def get_classes(db: Session = Depends(get_db)):
    return db.query(Class).all()


# ATTENDANCE ROUTES

@app.post("/attendance/")
def create_attendance(attendance: AttendanceSchema, db: Session = Depends(get_db)):
    new_attendance = Attendance(**attendance.dict())
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

@app.get("/attendance/")
def get_attendance(db: Session = Depends(get_db)):
    return db.query(Attendance).all()

# HOME ROUTE

@app.get("/")
def home():
    return {"message": "School Management API is running!"}