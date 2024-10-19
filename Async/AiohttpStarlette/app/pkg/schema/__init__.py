from app.pkg.schema.book import (
    BookSchema,
    CreateBookSchema,
    UpdateBookSchema,
    DeleteBookByNameSchema,
    GetBookByNameSchema,
)
from app.pkg.schema.author import (
    BookSchema,
    CreateAuthorSchema,
    AuthorSchema,
    DeleteAuthorByNameSchema,
    GetAuthorByNameSchema,
    UpdateAuthorSchema,
)
from app.pkg.schema.base import BaseSchema, HttpVerbs

__all__ = [
    # Book Schemas
    "BookSchema",
    "CreateBookSchema",
    "UpdateBookSchema",
    "DeleteBookByNameSchema",
    "GetBookByNameSchema",
    # Author Schemas
    "AuthorSchema",
    "CreateAuthorSchema",
    "DeleteAuthorByNameSchema",
    "GetAuthorByNameSchema",
    "UpdateAuthorSchema",
    # Base
    "BaseSchema",
    "HttpVerbs",
]
