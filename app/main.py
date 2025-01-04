from fastapi import FastAPI
from app.config.database import engine, Base
from app.posts import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router.router, prefix="/api", tags=["posts"])

@app.get("/")
def root():
    return {"message":"Welcome to my website"}
