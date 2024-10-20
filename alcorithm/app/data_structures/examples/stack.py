class Stack:
    def __init__(self):
        self._stack = []

    def push(self, value: int):
        self._stack.append(value)
        return self

    def pop(self):
        return self._stack.pop()


# Пример использования
stack = Stack()
stack.push(1).pop()  # >> 1
# >> stack = []
stack.push(1).push(2).push(3)
# >> stack = [1, 2, 3]
stack.pop()  # >> 3
# >> stack = [1, 2]
