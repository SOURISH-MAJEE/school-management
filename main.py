from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import engine, Base

from models import (
    teacher_model, student_model, subject_model,
    class_model, attendance_model, attendance_session_model
)

from routers import (
    teacher_router, student_router, subject_router,
    class_router, attendance_router, attendance_session_router
)

# ── ADD THIS LINE ──
from routers import auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(teacher_router.router)
app.include_router(student_router.router)
app.include_router(subject_router.router)
app.include_router(class_router.router)
app.include_router(attendance_router.router)
app.include_router(attendance_session_router.router)

# ── ADD THIS LINE ──
app.include_router(auth_router.router)

@app.get("/")
def home():
    return {"message": "School Management System API is running!"}