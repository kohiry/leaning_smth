from starlette.exceptions import HTTPException
import functools
from pydantic import ValidationError
from starlette.responses import JSONResponse
from aiohttp import web

__all__ = [
    "validate_request_aiohttp",
    "validate_request_starlette",
    "session_dependency",
]

from app.config import get_logger
from app.pkg.common import BaseSchema
from app.pkg.common.schema import HttpVerbs
from app.pkg.session import get_db_session

logger = get_logger()


def session_dependency(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        async with get_db_session() as session:
            return await func(*args, session=session, **kwargs)

    return wrapper


async def validate_request(
    request,
    schema: BaseSchema,
) -> tuple[BaseSchema | None, Exception | None]:
    try:
        data: dict | None = None
        if request.method == HttpVerbs.GET.value:
            data = request.query_params
        if request.method in [
            HttpVerbs.POST.value,
            HttpVerbs.DELETE.value,
            HttpVerbs.PUT.value,
        ]:
            data = await request.json()
        if data is None:
            raise ValidationError("Missed verbs")
        return schema.model_validate(dict(data)), None
    except ValidationError as e:
        logger.error(f"{request.base_url} = {e}")
        return None, e
    except TypeError as e:
        logger.error(f"{request.base_url} = {e}")
        return None, e


def validate_request_decorator(schema, response_class, error_raising):
    def decorator(func):
        @functools.wraps(func)  # save docs original func
        async def wrapper(self, request, *args, **kwargs):
            valid_data, error = await validate_request(request, schema)
            if error:
                raise error_raising(detail="Not valid data.", status_code=400)
            return await func(self=self, request=request, query=valid_data, **kwargs)

        return wrapper

    return decorator


# Fabric for decorators
# Для Starlette
def validate_request_starlette(schema: type[BaseSchema]):
    return validate_request_decorator(schema, JSONResponse, HTTPException)


# Для Aiohttp
def validate_request_aiohttp(schema: type[BaseSchema]):
    return validate_request_decorator(schema, web.json_response, "1")  # TODO заглушка
