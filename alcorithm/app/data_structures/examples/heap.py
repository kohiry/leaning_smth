from graphviz import Digraph


class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def extract_max(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_val

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]

    def draw_heap(self):
        """Строит схему дерева кучи."""
        dot = Digraph()
        for index, value in enumerate(self.heap):
            dot.node(str(index), str(value))  # Создание узлов
            # Добавляем рёбра (связи) для каждого узла
            if index > 0:
                parent_index = (index - 1) // 2
                dot.edge(
                    str(parent_index), str(index)
                )  # Соединяем родителя с дочерним узлом
        return dot


max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(20)
max_heap.insert(5)
max_heap.insert(30)
max_heap.insert(100)
max_heap.insert(1)
max_heap.insert(2)
max_heap.insert(3)
max_heap.insert(101)
max_heap.insert(102)


print(max_heap.extract_max())  # Вывод: 30

print(max_heap.peek())  # Вывод: 20
# Генерация и отображение схемы дерева кучи
heap_graph = max_heap.draw_heap()
heap_graph.render(
    "max_heap", format="png", cleanup=True
)  # Сохранить в файл max_heap.png
