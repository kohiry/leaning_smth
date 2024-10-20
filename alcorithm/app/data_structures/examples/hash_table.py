class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size  # определяем позицию (1, 2, 3, 4)

    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:  # одно из решений коллизии, метод цепочек
            if pair[0] == key:  # если да, обновляем
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:  # одно из решений коллизии, метод цепочек
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(
            self.table[index]
        ):  # одно из решений коллизии, метод цепочек
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def __repr__(self):
        """Возвращает строковое представление хеш-таблицы для удобства."""
        return str(self.table)


# Пример использования
hash_table = HashTable()

# Вставляем значения
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("grapes", 300)

# Получаем значения
print(hash_table.get("apple"))  # >> 100
print(hash_table.get("banana"))  # >> 200
print(hash_table.get("grapes"))  # >> 300
print(hash_table.get("orange"))  # >> None (нет такого ключа)

# Удаление значения
hash_table.delete("banana")
print(hash_table.get("banana"))  # >> None (ключ был удален)

# Вывод всей таблицы
print(hash_table)
