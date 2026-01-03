from sqlalchemy.orm import Session
from database import ConversationalEntityDB
from pydantic import BaseModel
from typing import List, Optional

# Pydantic models for API
class ConversationalEntityBase(BaseModel):
    name: str
    age: int
    grade: str

class ConversationalEntityCreate(ConversationalEntityBase):
    id: int

class ConversationalEntity(ConversationalEntityBase):
    id: int
    
    class Config:
        from_attributes = True

# CRUD operations
def create_entity(db: Session, entity: ConversationalEntityCreate):
    db_entity = ConversationalEntityDB(**entity.dict())
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity

def get_entity(db: Session, entity_id: int):
    return db.query(ConversationalEntityDB).filter(ConversationalEntityDB.id == entity_id).first()

<<<<<<< Updated upstream
def get_entities(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ConversationalEntityDB).offset(skip).limit(limit).all()
=======
# def get_entities(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(ConversationalEntityDB).offset(skip).limit(limit).all()
>>>>>>> Stashed changes

def update_entity(db: Session, entity_id: int, entity: ConversationalEntityCreate):
    db_entity = db.query(ConversationalEntityDB).filter(ConversationalEntityDB.id == entity_id).first()
    if db_entity:
        for key, value in entity.dict().items():
            setattr(db_entity, key, value)
        db.commit()
        db.refresh(db_entity)
    return db_entity

def delete_entity(db: Session, entity_id: int):
    db_entity = db.query(ConversationalEntityDB).filter(ConversationalEntityDB.id == entity_id).first()
    if db_entity:
        db.delete(db_entity)
        db.commit()
        return True
    return False

def entity_exists(db: Session, entity_id: int):
    result = db.query(ConversationalEntityDB).filter(ConversationalEntityDB.id == entity_id).first()
    return result is not None