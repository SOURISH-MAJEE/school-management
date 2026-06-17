from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.database import engine, Base

# Import all models so tables are created
from models import (
    teacher_model,
    student_model,
    subject_model,
    class_model,
    attendance_model,
    attendance_session_model
)

# Import all routers
from routers import (
    teacher_router,
    student_router,
    subject_router,
    class_router,
    attendance_router,
    attendance_session_router
)

# Create all tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="School Management System")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all routers
app.include_router(teacher_router.router)
app.include_router(student_router.router)
app.include_router(subject_router.router)
app.include_router(class_router.router)
app.include_router(attendance_router.router)
app.include_router(attendance_session_router.router)

@app.get("/")
def home():
    return {"message": "School Management System API is running!"}