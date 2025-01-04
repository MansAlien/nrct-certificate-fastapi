from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import get_db
from . import crud, schemas

router = APIRouter()

# Read posts list
@router.get("/posts/", response_model=list[schemas.Post])
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

# Read a post with id
@router.get("/posts/{post_id}", response_model=schemas.Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

# Create a post
@router.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db, post)

