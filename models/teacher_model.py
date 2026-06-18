from sqlalchemy import Column, Integer, String, Enum, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

teacher_subject = Table(
    "teacher_subject",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teacher.teacher_id"), primary_key=True),
    Column("subject_id", Integer, ForeignKey("subject.subject_id"), primary_key=True)
)

class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String(100), nullable=False)
    age        = Column(Integer, nullable=False)
    gender     = Column(Enum("Male", "Female", "Other"), nullable=False)
    email      = Column(String(100), unique=True, nullable=False)
    phone      = Column(String(15), nullable=False)

    subjects = relationship("Subject", secondary=teacher_subject, back_populates="teachers")