from enum import Enum

from app.alghoritms import alg_start
from app.data_structures import ds_start
from app.config import get_logger


class Topic(Enum):
    DATA_STRUCTURES = "Структуры данных"
    ALGHORITMS = "Алгоритмы"


logger = get_logger()


def app():
    logger.info(
        "Привет! Тут мы будем разбирать популярные алгоритмы и структуры данных :^D"
    )
    logger.info(
        f"""
Доступные топики:
1) {Topic.ALGHORITMS.value}
2) {Topic.DATA_STRUCTURES.value}
"""
    )
    choose = input("Выбери топик: 1, 2: \nВариант: ")
    if not choose.isalpha():
        return
    if int(choose) == 1:
        alg_start()
    elif int(choose) == 2:
        ds_start()


if __name__ == "__main__":
    while True:
        app()
