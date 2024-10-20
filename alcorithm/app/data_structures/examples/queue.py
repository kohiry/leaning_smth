from collections import deque


class Queue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, value: int):
        self._queue.append(value)
        return self

    def dequeue(self):
        return self._queue.popleft()


# Пример использования
queue = Queue()
queue.enqueue(1).enqueue(2).enqueue(3).dequeue()  # >> 1
# >> queue = [2, 3]
queue.dequeue()  # >> 2
queue.dequeue()  # >> 3
