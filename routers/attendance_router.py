from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.attendance_schema import AttendanceCreate, AttendanceUpdate, AttendanceResponse
from query import attendance_query

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/", response_model=AttendanceResponse)
def create_attendance(attendance: AttendanceCreate, db: Session = Depends(get_db)):
    return attendance_query.create_attendance(db, attendance)

@router.get("/", response_model=list[AttendanceResponse])
def get_attendance(db: Session = Depends(get_db)):
    return attendance_query.get_all_attendance(db)

@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_by_id(attendance_id: int, db: Session = Depends(get_db)):
    attendance = attendance_query.get_attendance_by_id(db, attendance_id)
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return attendance

@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(attendance_id: int, attendance: AttendanceUpdate, db: Session = Depends(get_db)):
    updated = attendance_query.update_attendance(db, attendance_id, attendance)
    if not updated:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return updated

@router.delete("/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    result = attendance_query.delete_attendance(db, attendance_id)
    if not result:
        raise HTTPException(status_code=404, detail="Attendance not found")
    return result