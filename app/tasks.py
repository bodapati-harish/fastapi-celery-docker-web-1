from celery import Celery

# Define the Celery application
celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",  # Redis will be in a separate container
    backend="redis://redis:6379/0"
)

@celery.task
def add_task(a: int, b: int):
    return a + b
