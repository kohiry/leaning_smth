from app.pkg.models import Base
from typing import List
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Book(Base):
    __tablename__ = "book"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False, unique=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("author.id"))
    author: Mapped["Author"] = relationship(
        back_populates="books",
    )

    def __repr__(self) -> str:
        return f"Book(id={self.id!r}, name={self.name!r}, author={self.author!r})"


class Author(Base):
    __tablename__ = "author"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(), nullable=False, unique=True)
    books: Mapped[List["Book"]] = relationship(
        back_populates="author",
    )

    def __repr__(self) -> str:
        return f"Author(id={self.id!r}, name={self.name!r})"
