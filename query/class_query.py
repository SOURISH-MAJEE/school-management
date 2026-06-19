from sqlalchemy.orm import Session
from models.class_model import Class
from schemas.class_schema import ClassCreate, ClassUpdate

def create_class(db: Session, cls: ClassCreate):
    new_class = Class(**cls.model_dump())
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class

def get_all_classes(db: Session):
    return db.query(Class).all()

def get_class_by_id(db: Session, class_id: int):
    return db.query(Class).filter(
        Class.class_id == class_id).first()

def update_class(db: Session, class_id: int, cls: ClassUpdate):
    db_class = db.query(Class).filter(
        Class.class_id == class_id).first()
    if not db_class:
        return None
    for key, value in cls.model_dump(exclude_unset=True).items():
        setattr(db_class, key, value)
    db.commit()
    db.refresh(db_class)
    return db_class

def delete_class(db: Session, class_id: int):
    db_class = db.query(Class).filter(
        Class.class_id == class_id).first()
    if not db_class:
        return None
    db.delete(db_class)
    db.commit()
    return {"message": "Class deleted successfully"}