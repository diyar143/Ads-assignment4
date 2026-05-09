import time
import random

class Vertex:
    def __init__(self, id_number):
        self.id = id_number

    def __str__(self):
        return f"Vertex {self.id}"

class Edge:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f"{self.source.id} -> {self.destination.id}"

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex.id not in self.adj_list:
            self.adj_list[vertex.id] = []

    def add_edge(self, from_id, to_id):
        if from_id in self.adj_list and to_id in self.adj_list:
            self.adj_list[from_id].append(to_id)

    def bfs(self, start_id):
        visited = set()
        queue = [start_id]
        visited.add(start_id)
        result = []

        while queue:
            current = queue.pop(0)
            result.append(str(current))
            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return " -> ".join(result)

    def dfs(self, start_id):
        visited = set()
        result = []

        def explore(current):
            visited.add(current)
            result.append(str(current))
            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    explore(neighbor)

        explore(start_id)
        return " -> ".join(result)

class Experiment:
    def run_tests(self):
        sizes = [10, 30, 100]
        for size in sizes:
            g = self.create_random_graph(size)

            start_bfs = time.perf_counter_ns()
            bfs_res = g.bfs(0)
            end_bfs = time.perf_counter_ns()

            start_dfs = time.perf_counter_ns()
            dfs_res = g.dfs(0)
            end_dfs = time.perf_counter_ns()

            print(f"Size: {size}")
            if size == 10:
                print(f"BFS: {bfs_res}")
                print(f"DFS: {dfs_res}")
            print(f"BFS Time: {end_bfs - start_bfs} ns")
            print(f"DFS Time: {end_dfs - start_dfs} ns\n")

    def create_random_graph(self, size):
        g = Graph()
        for i in range(size):
            g.add_vertex(Vertex(i))
        for _ in range(size * 2):
            g.add_edge(random.randint(0, size - 1), random.randint(0, size - 1))
        return g

if __name__ == "__main__":
    Experiment().run_tests()