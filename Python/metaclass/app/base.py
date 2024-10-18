from app.config import get_logger

__all__ = ["LogMetaClass"]

logger = get_logger()


class LogMetaClass(type):
    def __new__(cls, name, bases, dct):
        logger.info(f"Creating class: {name}")
        for key, value in dct.items():
            if callable(value):
                dct[key] = cls.log_method(value)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def log_method(method):
        def wrapper(*args, **kwargs):
            logger.info(f"Calling method {method.__name__}")
            return method(*args, **kwargs)

        return wrapper
