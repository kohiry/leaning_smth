from enum import Enum
from pydantic import BaseModel


class BaseScheme(BaseModel):
    pass


class HttpVerbs(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"
