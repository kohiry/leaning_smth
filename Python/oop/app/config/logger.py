import logging


def get_logger(name=__name__):
    """
    Создает и возвращает логгер с заданным именем.
    По умолчанию используется имя модуля (__name__).
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Создаем консольный обработчик
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # Форматтер для вывода сообщений
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    ch.setFormatter(formatter)

    # Добавляем обработчик к логгеру
    logger.addHandler(ch)

    return logger
