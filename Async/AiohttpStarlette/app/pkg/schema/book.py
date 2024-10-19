from app.pkg.common import BaseSchema


class BaseBookSchema(BaseSchema):
    pass


class GetBookByNameSchema(BaseBookSchema):
    name: str


class CreateBookSchema(BaseBookSchema):
    name: str
    author: str


class UpdateBookSchema(BaseBookSchema):
    old_name: str
    name: str
    author: str


class DeleteBookByNameSchema(BaseBookSchema):
    name: str


class BookSchema(BaseBookSchema):
    name: str
    author: str
