class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        """Вспомогательный метод для рекурсивного добавления узла"""
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add(node.right, value)

    def find(self, value):
        return self._find(self.root, value)

    def _find(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._find(node.left, value)
        else:
            return self._find(node.right, value)

    def inorder_traversal(self):
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, values):
        if node:
            self._inorder_traversal(node.left, values)
            values.append(node.value)
            self._inorder_traversal(node.right, values)
        return values

    def __repr__(self):
        return f"BinaryTree({self.inorder_traversal()})"


# Пример использования
bt = BinaryTree()
bt.add(5)
bt.add(2)
bt.add(8)
bt.add(1)
bt.add(3)

print(bt)  # Вывод: BinaryTree([1, 2, 3, 5, 8])

print(bt.find(3))  # Вывод: True
print(bt.find(10))  # Вывод: False
