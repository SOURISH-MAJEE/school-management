from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

student_class = Table(
    "student_class",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("student.student_id")),
    Column("class_id", Integer, ForeignKey("class.class_id"))
)

class Class(Base):
    __tablename__ = "class"

    class_id = Column(Integer, primary_key=True, autoincrement=True)
    class_name = Column(String(50), nullable=False)

    students = relationship("Student", secondary=student_class, back_populates="classes")