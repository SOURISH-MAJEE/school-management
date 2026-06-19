from sqlalchemy.orm import Session
from models.attendance_session_model import AttendanceSession
from schemas.attendance_session_schema import (
    AttendanceSessionCreate, AttendanceSessionUpdate)

def create_session(db: Session, session: AttendanceSessionCreate):
    new_session = AttendanceSession(**session.model_dump())
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

def get_all_sessions(db: Session):
    return db.query(AttendanceSession).all()

def get_session_by_id(db: Session, session_id: int):
    return db.query(AttendanceSession).filter(
        AttendanceSession.session_id == session_id).first()

def get_sessions_by_class(db: Session, class_id: int):
    return db.query(AttendanceSession).filter(
        AttendanceSession.class_id == class_id).all()

def update_session(db: Session, session_id: int,
                   session: AttendanceSessionUpdate):
    db_session = db.query(AttendanceSession).filter(
        AttendanceSession.session_id == session_id).first()
    if not db_session:
        return None
    for key, value in session.model_dump(exclude_unset=True).items():
        setattr(db_session, key, value)
    db.commit()
    db.refresh(db_session)
    return db_session

def delete_session(db: Session, session_id: int):
    db_session = db.query(AttendanceSession).filter(
        AttendanceSession.session_id == session_id).first()
    if not db_session:
        return None
    db.delete(db_session)
    db.commit()
    return {"message": "Session deleted successfully"}