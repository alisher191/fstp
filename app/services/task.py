from sqlalchemy.orm import Session
from app.repositories.task import TaskRepository
from app.schemas.task import TaskUpdateSchema, TaskCreateSchema, TaskSchema


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)

    def list_tasks(self, ) -> list[TaskSchema]:
        tasks_list = self.task_repository.get_all()
        return [TaskSchema.model_validate(task) for task in tasks_list]

    def create_task(self, task_create: TaskCreateSchema) -> TaskSchema:
        new_task = self.task_repository.create(title=task_create.title)
        self.db.commit()
        return TaskSchema.model_validate(new_task)

    def update_task(self, task_id: str, task_update: TaskUpdateSchema) -> TaskSchema:
        task_for_update = self.task_repository.get_by_id(task_id=task_id)
        if task_update.title:
            task_for_update.title = task_update.title
        if task_update.completed:
            task_for_update.completed = task_update.completed
        else:
            task_for_update.completed = False
        self.db.commit()
        return TaskSchema.model_validate(task_for_update)

    def delete_task(self, task_id: str) -> None:
        task_for_delete = self.task_repository.get_by_id(task_id=task_id)
        self.task_repository.delete(task_for_delete)
