from fastapi import FastAPI
from app.config.database import engine, Base
from app.posts import router as posts_router
from app.users import router as users_router
from app.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.router, prefix="/api/auth", tags=["auth"])
app.include_router(users_router.router, prefix="/api/users", tags=["users"])
app.include_router(posts_router.router, prefix="/api/posts", tags=["posts"])

@app.get("/")
def root():
    return {"message":"Welcome to my website"}
