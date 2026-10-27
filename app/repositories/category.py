from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.category import CategoryORM


class CategoryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_all(self) -> list[CategoryORM]:
        return list(self.db.scalars(select(CategoryORM)).all())

    def get_by_id(self, category_id: str) -> CategoryORM:
        return self.db.get(CategoryORM, category_id)

    def create(self, name: str) -> CategoryORM:
        category = CategoryORM(name=name)
        self.db.add(category)
        self.db.flush()
        self.db.commit()
        self.db.refresh(category)
        return category

    def delete(self, CategoryORM) -> None:
        if CategoryORM is None:
            raise FileNotFoundError
        self.db.delete(CategoryORM)
        self.db.commit()
