import os
from enum import Enum

from app.common import clear_console
from app.config import get_logger
from app.data_structures.services import *

# Логгер для вывода сообщений
logger = get_logger()


# Класс перечисления базовых структур данных
class DataStructures(Enum):
    ARRAY = "Array (Массив)"
    LINKED_LIST = "Linked List (Связный список)"
    STACK = "Stack (Стек)"
    QUEUE = "Queue (Очередь)"
    HASH_TABLE = "Hash Table (Хеш-таблица)"
    SET = "Set (Множество)"
    BINARY_TREE = "Binary Tree (Бинарное дерево)"
    BINARY_SEARCH_TREE = "Binary Search Tree (Бинарное дерево поиска)"
    HEAP = "Heap (Куча)"
    GRAPH = "Graph (Граф)"


# Функция для обработки структур данных
def ds_start():
    logger.info("Вы выбрали тему: Структуры данных!")

    # Вывод доступных структур данных
    logger.info("Доступные структуры данных:")
    for idx, ds in enumerate(DataStructures, 1):
        logger.info(f"{idx}) {ds.value}")

    # Получаем выбор пользователя
    choose = input(f"Выбери структуру данных (1-{len(DataStructures)}): \nВариант: ")
    clear_console()
    # Проверка на корректность ввода
    if not choose.isdigit() or not (1 <= int(choose) <= len(DataStructures)):
        logger.error("Некорректный выбор. Пожалуйста, выберите правильный номер.")
        return

    # Получение выбранной структуры данных
    chosen_structure = list(DataStructures)[int(choose) - 1]
    logger.info(f"Вы выбрали: {chosen_structure.value}")
    logger.info("\n")

    # Вызов соответствующей функции теории
    if chosen_structure == DataStructures.ARRAY:
        explain_array()
    elif chosen_structure == DataStructures.LINKED_LIST:
        explain_linked_list()
    elif chosen_structure == DataStructures.STACK:
        explain_stack()
    elif chosen_structure == DataStructures.QUEUE:
        explain_queue()
    elif chosen_structure == DataStructures.HASH_TABLE:
        explain_hash_table()
    elif chosen_structure == DataStructures.SET:
        explain_set()
    elif chosen_structure == DataStructures.BINARY_TREE:
        explain_binary_tree()
    elif chosen_structure == DataStructures.BINARY_SEARCH_TREE:
        explain_binary_search_tree()
    elif chosen_structure == DataStructures.HEAP:
        explain_heap()
    elif chosen_structure == DataStructures.GRAPH:
        explain_graph()
    logger.info("\n")
    input("Press Enter to restart")
