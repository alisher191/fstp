from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base import Base


class CategoryORM(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String, index=True)
