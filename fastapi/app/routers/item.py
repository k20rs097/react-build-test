# app/routers/item.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, models, database
import schemas.item as item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

@router.post("/", response_model=item.Item)
def create_item(item: item.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = models.Item(title=item.title, description=item.description, owner_id=1)  # For simplicity
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/{item_id}", response_model=item.Item)
def read_item(item_id: int, db: Session = Depends(database.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
