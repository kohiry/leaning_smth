"""
Довольно плохое и не масштабируемое решение, сделанное на скорую руку.
Можно было накинуть несколько прослоек и абстракций, чтобы было более универсально.
"""

from starlette.requests import Request

from starlette.exceptions import HTTPException
import functools
from pydantic import ValidationError
from aiohttp.web import HTTPBadRequest

from app.config import get_logger
from app.pkg.common import BaseSchema
from app.pkg.common.schema import HttpVerbs
from app.pkg.session import get_db_session

__all__ = [
    "validate_request_aiohttp",
    "validate_request_starlette",
    "session_dependency",
]


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
            # query_params = starlette | query = aiohttp
            data = (
                hasattr(request, "query_params")
                and request.query_params
                or request.query
            )
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
        logger.error(f"{e}")
        return None, e
    except TypeError as e:
        logger.error(f"{e}")
        return None, e


def validate_request_decorator(schema, error_raising):
    def decorator(func):
        @functools.wraps(func)  # save docs original func
        async def wrapper(self, *args, **kwargs):
            # args = starlette | self.request = aiohttp
            if args and type(args[0]) is Request:
                request = args[0]
            else:
                request = self.request
            valid_data, error = await validate_request(request, schema)
            if error:
                # detail = starlette | text = aiohttp
                if hasattr(error_raising, "detail"):
                    raise error_raising(detail="Not valid data.", status_code=400)
                raise error_raising(text="Not valid data.")
            return await func(self, *args, query=valid_data, **kwargs)

        return wrapper

    return decorator


# Fabric for decorators
# For Starlette
def validate_request_starlette(schema: type[BaseSchema]):
    return validate_request_decorator(schema, HTTPException)


# For Aiohttp
def validate_request_aiohttp(schema: type[BaseSchema]):
    return validate_request_decorator(schema, HTTPBadRequest)
