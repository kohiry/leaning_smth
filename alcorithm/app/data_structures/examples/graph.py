from graphviz import Digraph


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_vertex)
        print(start_vertex)
        for neighbor in self.adjacency_list[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def visualize(self, filename="graph"):
        """Создает визуальное представление графа и сохраняет его в файл."""
        dot = Digraph(comment="Graph")

        for vertex in self.adjacency_list:
            dot.node(str(vertex))  # Добавляем вершину в граф

        for vertex, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                dot.edge(str(vertex), str(neighbor))  # Добавляем рёбра

        dot.render(
            filename, format="png", cleanup=True
        )  # Сохраняем граф в файл в формате PNG
        print(f"Graph visualized and saved as {filename}.png")

    def __repr__(self):
        """Возвращает строковое представление графа."""
        return f"Graph({self.adjacency_list})"


# Пример использования
graph = Graph()
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 4)
graph.add_edge(3, 2)

print(graph)  # Вывод: Graph({1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]})

# Выполнение обхода в глубину, начиная с вершины 1
print("DFS starting from vertex 1:")
graph.dfs(1)

graph.visualize("my_graph")
