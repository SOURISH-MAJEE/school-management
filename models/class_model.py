from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class Class(Base):
    __tablename__ = "class"

    class_id   = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50), nullable=False)
    section    = Column(String(10), nullable=False)

    # One class has many students
    students = relationship("Student", back_populates="student_class")