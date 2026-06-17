from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

teacher_subject = Table(
    "teacher_subject",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teacher.teacher_id")),
    Column("subject_id", Integer, ForeignKey("subject.subject_id"))
)

class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(15))

    subjects = relationship("Subject", secondary=teacher_subject, back_populates="teachers")