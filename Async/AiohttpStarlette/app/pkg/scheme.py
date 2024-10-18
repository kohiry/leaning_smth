from pydantic import BaseModel

__all__ = ["Book"]


class Book(BaseModel):
    name: str
    author: str
