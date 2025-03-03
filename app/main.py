from fastapi import FastAPI
from app.tasks import add_task

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

@app.post("/add/")
def add_numbers(a: int, b: int):
    result = add_task.delay(a, b)  # Celery task
    return {"task_id": result.id, "message": "Task submitted"}
