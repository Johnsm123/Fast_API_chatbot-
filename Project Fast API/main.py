from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db, create_tables
from crud import (
    create_entity as crud_create_entity,
    get_entity as crud_get_entity,
<<<<<<< Updated upstream
    get_entities as crud_get_entities,
=======
>>>>>>> Stashed changes
    update_entity as crud_update_entity,
    delete_entity as crud_delete_entity,
    entity_exists,
    ConversationalEntity,
    ConversationalEntityCreate
)

# Create FastAPI app
app = FastAPI(title="Intelligent Conversational AI Management API")

# Create database tables on startup
@app.on_event("startup")
def startup_event():
    create_tables()

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Intelligent Conversational AI Management API"}

# Create entity
@app.post("/entities", response_model=ConversationalEntity)
def create_entity(entity: ConversationalEntityCreate, db: Session = Depends(get_db)):
    if entity_exists(db, entity.id):
        raise HTTPException(status_code=400, detail=f"Entity with ID {entity.id} already exists")
    
    created_entity = crud_create_entity(db=db, entity=entity)
    return created_entity

<<<<<<< Updated upstream
# Get all entities
@app.get("/entities", response_model=List[ConversationalEntity])
def get_entities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_get_entities(db, skip=skip, limit=limit)

# Get entity by ID
@app.get("/entities/{entity_id}", response_model=ConversationalEntity)
def get_entity(entity_id: int, db: Session = Depends(get_db)):
    db_entity = crud_get_entity(db, entity_id=entity_id)
    if db_entity is None:
        raise HTTPException(status_code=404, detail=f"Entity with ID {entity_id} not found")
    return db_entity

# Update entity
@app.put("/entities/{entity_id}", response_model=ConversationalEntity)
def update_entity(entity_id: int, entity: ConversationalEntityCreate, db: Session = Depends(get_db)):
    if entity.id != entity_id:
        raise HTTPException(status_code=400, detail=f"Entity ID in path ({entity_id}) must match ID in request body ({entity.id})")
    
    if not entity_exists(db, entity_id):
        raise HTTPException(status_code=404, detail=f"Entity with ID {entity_id} not found")
    
    db_entity = crud_update_entity(db=db, entity_id=entity_id, entity=entity)
    return db_entity

=======
# Get entity by ID
@app.get("/entities/{entity_id}", response_model=ConversationalEntity)
def get_entity(entity_id: int, db: Session = Depends(get_db)):
    db_entity = crud_get_entity(db, entity_id=entity_id)
    if db_entity is None:
        raise HTTPException(status_code=404, detail=f"Entity with ID {entity_id} not found")
    return db_entity

# Update entity
@app.put("/entities/{entity_id}", response_model=ConversationalEntity)
def update_entity(entity_id: int, entity: ConversationalEntityCreate, db: Session = Depends(get_db)):
    if entity.id != entity_id:
        raise HTTPException(status_code=400, detail=f"Entity ID in path ({entity_id}) must match ID in request body ({entity.id})")
    
    if not entity_exists(db, entity_id):
        raise HTTPException(status_code=404, detail=f"Entity with ID {entity_id} not found")
    
    db_entity = crud_update_entity(db=db, entity_id=entity_id, entity=entity)
    return db_entity

>>>>>>> Stashed changes
# Delete entity
@app.delete("/entities/{entity_id}")
def delete_entity(entity_id: int, db: Session = Depends(get_db)):
    if not entity_exists(db, entity_id):
        raise HTTPException(status_code=404, detail=f"Entity with ID {entity_id} not found")
    
    crud_delete_entity(db=db, entity_id=entity_id)
    return {"message": f"Entity with ID {entity_id} deleted successfully"}
