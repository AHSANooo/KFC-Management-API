# main.py
from fastapi import FastAPI
from api.auth.endpoints import router as auth_router
from tasks.endpoints import router as tasks_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the KFC Order Management API"}
