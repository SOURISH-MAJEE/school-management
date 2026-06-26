from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Student(Base):
    __tablename__ = "student"

    student_id  = Column(Integer, primary_key=True, autoincrement=True)
    roll_number = Column(String(20), unique=True, nullable=False)
    name        = Column(String(100), nullable=False)
    age         = Column(Integer, nullable=False)
    gender      = Column(Enum("Male", "Female", "Other"), nullable=False)
    phone       = Column(String(15))
    class_id    = Column(Integer, ForeignKey("class.class_id"), nullable=False)
    password    = Column(String(255), nullable=False)

    student_class = relationship("Class", back_populates="students")