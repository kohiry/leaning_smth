from app.pkg.schema.base import BaseScheme
from app.pkg.schema.book import BookSchema


class BaseAuthorSchema(BaseScheme):
    pass


class GetAuthorByNameSchema(BaseAuthorSchema):
    name: str


class CreateAuthorSchema(BaseAuthorSchema):
    name: str


class UpdateAuthorSchema(BaseAuthorSchema):
    name: str


class DeleteAuthorByNameSchema(BaseAuthorSchema):
    name: str


class AuthorSchema(BaseAuthorSchema):
    name: str
    books: list[BookSchema]
