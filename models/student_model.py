from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from database.database import Base
from models.class_model import student_class
import datetime

class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(15))
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    classes = relationship("Class", secondary=student_class, back_populates="students")