import pprint

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database
import schemas.user as schema

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(database.get_db)):
    db_user = schema.User(name=user.name, email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
