from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.auth import get_current_user
from app.config.database import get_db
from app.users import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@router.get("/me", response_model=schemas.User)
def read_current_user(current_user: schemas.User = Depends(get_current_user)):
    return current_user

@router.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.get_users(db)

@router.get("/{username}", response_model=schemas.User)
def read_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

