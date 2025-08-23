from fastapi import FastAPI
from app.routers import blog, health
from app.db import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog Workflow API")

# Include routers
app.include_router(blog.router)
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "FastAPI Blog Workflow is running 🚀"}
