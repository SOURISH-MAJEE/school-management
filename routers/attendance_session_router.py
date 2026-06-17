from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.attendance_session_schema import AttendanceSessionCreate, AttendanceSessionUpdate, AttendanceSessionResponse
from query import attendance_session_query

router = APIRouter(prefix="/attendance-sessions", tags=["Attendance Sessions"])

@router.post("/", response_model=AttendanceSessionResponse)
def create_session(session: AttendanceSessionCreate, db: Session = Depends(get_db)):
    return attendance_session_query.create_session(db, session)

@router.get("/", response_model=list[AttendanceSessionResponse])
def get_sessions(db: Session = Depends(get_db)):
    return attendance_session_query.get_all_sessions(db)

@router.get("/{session_id}", response_model=AttendanceSessionResponse)
def get_session(session_id: int, db: Session = Depends(get_db)):
    session = attendance_session_query.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session

@router.put("/{session_id}", response_model=AttendanceSessionResponse)
def update_session(session_id: int, session: AttendanceSessionUpdate, db: Session = Depends(get_db)):
    updated = attendance_session_query.update_session(db, session_id, session)
    if not updated:
        raise HTTPException(status_code=404, detail="Session not found")
    return updated

@router.delete("/{session_id}")
def delete_session(session_id: int, db: Session = Depends(get_db)):
    result = attendance_session_query.delete_session(db, session_id)
    if not result:
        raise HTTPException(status_code=404, detail="Session not found")
    return result