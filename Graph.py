from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start_node):
        visited = set([start_node])
        queue = deque([start_node])
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_node, visited=None, result=None):
        if visited is None:
            visited = set()
        if result is None:
            result = []

        visited.add(start_node)
        result.append(start_node)

        for neighbor in self.adj_list.get(start_node, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited, result)
        return result

if __name__ == "__main__":
    print("--- GRAPH (COSINO) ---")
    g = Graph()
    # Graph Edges connecting nodes: C, O, S, I, N
    edges = [('C', 'O'), ('C', 'S'), ('O', 'I'), ('O', 'N'), ('I', 'N'), ('S', 'N')]
    for u, v in edges:
        g.add_edge(u, v)

    print("BFS Traversal (starting at C):", " -> ".join(g.bfs('C')))
    print("DFS Traversal (starting at C):", " -> ".join(g.dfs('C')))