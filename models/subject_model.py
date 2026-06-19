from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Subject(Base):
    __tablename__ = "subject"

    subject_id   = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(100), nullable=False)
    teacher_id   = Column(Integer, ForeignKey("teacher.teacher_id"),
                          nullable=True)

    # Many subjects belong to one teacher
    teacher = relationship("Teacher", back_populates="subjects")