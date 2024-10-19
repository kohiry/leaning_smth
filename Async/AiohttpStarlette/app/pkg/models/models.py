from app.pkg.models import BaseModel
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String


class BookModel(BaseModel):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(), nullable=False)

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, name={self.name!r}, author={self.author!r})"
