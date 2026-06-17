from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class AttendanceSession(Base):
    __tablename__ = "attendance_session"

    session_id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey("class.class_id"))
    subject_id = Column(Integer, ForeignKey("subject.subject_id"))
    date = Column(Date, nullable=False)
    period = Column(Integer, nullable=False)

    attendances = relationship("Attendance", back_populates="session")