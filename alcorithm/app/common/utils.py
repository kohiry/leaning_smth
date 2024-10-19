import os


def clear_console():
    """Очистить консоль."""
    os.system("cls" if os.name == "nt" else "clear")
