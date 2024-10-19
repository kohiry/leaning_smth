"""
    На этапе разработки, обнаружил проблему с разными http глалголами и посчитал,
не релевыантным дальнейшую разработку подхода, оставлю как интересный пример, но не
рабочий.
"""

from contextlib import asynccontextmanager

from pydantic import BaseModel
import functools
from pydantic import ValidationError
from starlette.responses import JSONResponse
from aiohttp import web

__all__ = [
    "validate_request_aiohttp",
    "validate_request_starlette",
    "session_dependency",
]

from app.pkg.session import get_db_session


def session_dependency(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        async with get_db_session() as session:
            return await func(*args, session=session, **kwargs)

    return wrapper


async def validate_request(request, schema):
    try:
        data = await request.json()
        return schema(**data), None
    except ValidationError as e:
        return None, e


def validate_request_decorator(schema, response_class):
    def decorator(func):
        @functools.wraps(func)  # save docs original func
        async def wrapper(request, *args, **kwargs):
            valid_data, error = await validate_request(request, schema)
            if error:
                return response_class({"error": error.errors()}, status_code=400)
            return await func(request, valid_data, *args, **kwargs)

        return wrapper

    return decorator


# Fabric for decorators
# Для Starlette
def validate_request_starlette(schema: BaseModel):
    return validate_request_decorator(schema, JSONResponse)


# Для Aiohttp
def validate_request_aiohttp(schema: BaseModel):
    return validate_request_decorator(schema, web.json_response)
