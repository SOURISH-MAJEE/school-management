from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base
from models.teacher_model import teacher_subject

class Subject(Base):
    __tablename__ = "subject"

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String(100), nullable=False)

    teachers = relationship("Teacher", secondary=teacher_subject, back_populates="subjects")