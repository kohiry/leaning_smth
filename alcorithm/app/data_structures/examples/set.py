"""
Set реализована на линейном пробировании. More about collision, move to hash_table
"""


class MySet:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size
        self.count = 0  # количество элементов в множестве

    def _hash(self, value):
        return hash(value) % self.size

    def add(self, value):
        if self.contains(value):
            return

        index = self._hash(value)
        if self.table[index] is None:
            self.table[index] = value
        else:
            # Обработка коллизий с линейным пробированием
            while self.table[index] is not None:  # делаем лютый + 1 пока не будет None
                index = (index + 1) % self.size
                print("Колиззия!")
            self.table[index] = value
        self.count += 1

        if self.count / self.size > 0.7:
            self._resize()

    def contains(self, value):
        index = self._hash(value)

        while self.table[index] is not None:
            if self.table[index] == value:
                return True
            index = (index + 1) % self.size
        return False

    def remove(self, value):
        index = self._hash(value)
        while self.table[index] is not None:
            if self.table[index] == value:
                self.table[index] = None
                self.count -= 1
                return
            index = (index + 1) % self.size

    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size

        for value in old_table:  # рехешируем
            if value is not None:
                self.add(value)


myset = MySet()
myset.add(2)
myset.add(3)  # [.., None, 2, 3, None, ..]
myset.add(3)  # [.., None, 2, 3, None, ..]
myset.remove(3)  # [.., None, 2, None, None, ..]
myset.contains(3)  # False
myset.add("zxc")
