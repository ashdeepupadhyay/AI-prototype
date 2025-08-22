from fastapi import APIRouter, HTTPException
from app import crud, schemas
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = next(get_db())):
    db_item = crud.create_item(db=db, item=item)
    return db_item

@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = next(get_db())):
    db_item = crud.get_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/items/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, item: schemas.ItemUpdate, db: Session = next(get_db())):
    db_item = crud.update_item(db=db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.delete("/items/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = next(get_db())):
    db_item = crud.delete_item(db=db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

def include_router(app):
    app.include_router(router)