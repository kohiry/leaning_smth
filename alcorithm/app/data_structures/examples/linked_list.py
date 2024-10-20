class LinkedList:
    def __init__(self, value, next_val=None):
        self.value = value
        self.next_val = None


# [1, 2, 3, 4]
head = LinkedList(
    value=1,
    next_val=LinkedList(
        value=2,
        next_val=LinkedList(value=3, next_val=LinkedList(value=4, next_val=None)),
    ),
)
# Простой пример связного списка.
# В основном на низком уровне, так устроенны массивы, каждый элемент связан с предыдущим
# К примеру в С, мы можем выйти за указатель, но в целом массив устроен так же
