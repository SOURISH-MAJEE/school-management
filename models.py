from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(15))

class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.teacher_id"))

class Class(Base):
    __tablename__ = "class"

    class_id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50), nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))

class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(15))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.student_id"))
    class_id = Column(Integer, ForeignKey("class.class_id"))
    date = Column(Date, nullable=False)
    status = Column(Enum("Present", "Absent", "Late"), nullable=False)