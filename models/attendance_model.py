from sqlalchemy import Column, Integer, Enum, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True, autoincrement=True)
    session_id    = Column(Integer, ForeignKey("attendance_session.session_id"),
                           nullable=False)
    student_id    = Column(Integer, ForeignKey("student.student_id"),
                           nullable=False)
    status        = Column(Enum("Present", "Absent", "Late"), nullable=False)

    # Many attendance records belong to one session
    session = relationship("AttendanceSession", back_populates="attendances")