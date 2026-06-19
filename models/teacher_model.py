from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from database.database import Base

class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String(100), nullable=False)
    age        = Column(Integer, nullable=False)
    gender     = Column(Enum("Male", "Female", "Other"), nullable=False)
    email      = Column(String(100), unique=True, nullable=False)
    phone      = Column(String(15), nullable=False)

    # One teacher teaches many subjects
    subjects = relationship("Subject", back_populates="teacher")