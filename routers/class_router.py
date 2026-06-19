from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from schemas.class_schema import ClassCreate, ClassUpdate, ClassResponse
from query import class_query

router = APIRouter(prefix="/classes", tags=["Classes"])

@router.post("/", response_model=ClassResponse)
def create_class(cls: ClassCreate, db: Session = Depends(get_db)):
    return class_query.create_class(db, cls)

@router.get("/", response_model=list[ClassResponse])
def get_classes(db: Session = Depends(get_db)):
    return class_query.get_all_classes(db)

@router.get("/{class_id}", response_model=ClassResponse)
def get_class(class_id: int, db: Session = Depends(get_db)):
    cls = class_query.get_class_by_id(db, class_id)
    if not cls:
        raise HTTPException(status_code=404, detail="Class not found")
    return cls

@router.put("/{class_id}", response_model=ClassResponse)
def update_class(class_id: int, cls: ClassUpdate,
                 db: Session = Depends(get_db)):
    updated = class_query.update_class(db, class_id, cls)
    if not updated:
        raise HTTPException(status_code=404, detail="Class not found")
    return updated

@router.delete("/{class_id}")
def delete_class(class_id: int, db: Session = Depends(get_db)):
    result = class_query.delete_class(db, class_id)
    if not result:
        raise HTTPException(status_code=404, detail="Class not found")
    return result