from sqlalchemy.orm import Session
from models.attendance_model import Attendance
from schemas.attendance_schema import AttendanceCreate, AttendanceUpdate

def create_attendance(db: Session, attendance: AttendanceCreate):
    new_attendance = Attendance(**attendance.model_dump())
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return new_attendance

def get_all_attendance(db: Session):
    return db.query(Attendance).all()

def get_attendance_by_id(db: Session, attendance_id: int):
    return db.query(Attendance).filter(
        Attendance.attendance_id == attendance_id).first()

def get_attendance_by_session(db: Session, session_id: int):
    return db.query(Attendance).filter(
        Attendance.session_id == session_id).all()

def get_attendance_by_student(db: Session, student_id: int):
    return db.query(Attendance).filter(
        Attendance.student_id == student_id).all()

def update_attendance(db: Session, attendance_id: int,
                      attendance: AttendanceUpdate):
    db_attendance = db.query(Attendance).filter(
        Attendance.attendance_id == attendance_id).first()
    if not db_attendance:
        return None
    for key, value in attendance.model_dump(exclude_unset=True).items():
        setattr(db_attendance, key, value)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

def delete_attendance(db: Session, attendance_id: int):
    db_attendance = db.query(Attendance).filter(
        Attendance.attendance_id == attendance_id).first()
    if not db_attendance:
        return None
    db.delete(db_attendance)
    db.commit()
    return {"message": "Attendance deleted successfully"}