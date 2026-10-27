from fastapi import Depends
from sqlalchemy.orm import Session

from app.services.category import CategoryService
from app.services.task import TaskService
from app.db.session import get_db



def get_task_service(db: Session = Depends(get_db)):
    return TaskService(db=db)

def get_category_service(db: Session = Depends(get_db)):
    return CategoryService(db=db)
