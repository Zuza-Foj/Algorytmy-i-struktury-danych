import graphviz
import sys
from queue_from_l_3 import Queue

class Graph:
    def __init__(self):
        self.list_of_verts = []
        self.list_of_edges = []
        self.adjacency_list = {}

    def add_vertex(self, vert):
        if vert not in self.list_of_verts:
            self.list_of_verts.append(vert)
            self.adjacency_list[vert] = []

    def add_vertices_from_list(self, vert_list):
        for vert in vert_list:
            self.add_vertex(vert)

    def add_edge(self, from_vert, to_vert, weight=1):
        self.add_vertex(from_vert)
        self.add_vertex(to_vert)

        edge = (from_vert, to_vert, weight)
        if edge not in self.list_of_edges:
            self.list_of_edges.append(edge)
            self.adjacency_list[from_vert].append((to_vert, weight))

    def add_edges_from_list(self, edge_list):
        for edge in edge_list:
            if len(edge) == 2:
                self.add_edge(edge[0], edge[1])
            elif len(edge) == 3:
                self.add_edge(edge[0], edge[1], edge[2])

    def get_vertices(self):
        return self.list_of_verts.copy()

    def get_edges(self):
        return self.list_of_edges.copy()

    def get_neighbors(self, vert_key):
        if vert_key in self.adjacency_list:
            return [neighbor for neighbor, weight in self.adjacency_list[vert_key]]    # rozpakowuje tuple i zwraca tylko neighbour
        return []

    def contains(self, vert):
        return vert in self.list_of_verts

# zad 2.
    def save_graph(self, filename='graph.dot'):
        with open(filename, 'w') as f:
            f.write("digraph Graph {\n")

            for vert in self.list_of_verts:
                f.write(f'    "{vert}";\n')

            for from_vert, to_vert, weight in self.list_of_edges:
                if weight != 1:
                    f.write(f'    "{from_vert}" -> "{to_vert}" [label="{weight}"];\n')
                else:
                    f.write(f'    "{from_vert}" -> "{to_vert}";\n')

            f.write("}\n")
        print(f"Graf zapisany do pliku: {filename}")


    def draw(self, filename='Graph'):
        dot = graphviz.Digraph(comment='Graph')

        for vert in self.list_of_verts:
            dot.node(str(vert))

        for from_vert, to_vert, weight in self.list_of_edges:
            if weight != 1:
                dot.edge(str(from_vert), str(to_vert), label=str(weight))
            else:
                dot.edge(str(from_vert), str(to_vert))

        dot.render(filename, format='png', cleanup=True)
        return

# zad 3.
    def bfs(self, start_vert):
        if start_vert not in self.list_of_verts:
            print(f"Wierzchołek {start_vert} nie istnieje w grafie!")
            return []

        visited = []
        queue = Queue()
        queue.enqueue(start_vert)
        visited.append(start_vert)

        while not queue.is_empty():
            current = queue.dequeue()
            print(f"Odwiedzam: {current}")
            for neighbor in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.enqueue(neighbor)

        return visited

    def dfs_rec(self, start_vert, visited=None):
        if visited is None:
            return []

        if start_vert not in self.list_of_verts:    # stopuje rekurencję, jeśli nie ma takiego wierzchołka
            return visited

        visited.append(start_vert)
        for neighbor in self.get_neighbors(start_vert):
            if neighbor not in visited:
                self.dfs_rec(neighbor, visited)

        return visited

# zad 4.
    def topological_sort(self):
        visited = set()
        stack = []

        def dfs_topo(v):
            visited.add(v)
            for neighbour in self.get_neighbors(v):
                if neighbour not in visited:
                    dfs_topo(neighbour)
            stack.append(v)

        for vertex in self.list_of_verts:
            if vertex not in visited:
                dfs_topo(vertex)
        return stack[::-1]

# zad 5.
    def shortest_paths_bfs(self, start_vert):
        if start_vert not in self.list_of_verts:
            return None

        distances = {vert: float('inf') for vert in self.list_of_verts}    # jak daleko dany wierzchołek znajduje się od początku
        predecessors = {vert: None for vert in self.list_of_verts}    # skąd przechodzę do kolejnego wierzchołka
        distances[start_vert] = 0
        queue = Queue()
        queue.enqueue(start_vert)

        while not queue.is_empty():
            current = queue.dequeue()
            for neighbor in self.get_neighbors(current):
                if distances[neighbor] == float('inf'):  # If not visited
                    distances[neighbor] = distances[current] + 1
                    predecessors[neighbor] = current
                    queue.enqueue(neighbor)

        return distances, predecessors

if __name__ == '__main__':
    g = Graph()
    g.add_vertices_from_list(['A', 'B', 'C', 'D', 'E'])
    g.add_edges_from_list([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')])

    g.draw()
    g.save_graph()

    print(f"Ścieżka BFS: {g.bfs('A')}")
    print(f"Ścieżka DFS: {g.dfs_rec('A', [])}")

    dag = Graph()
    dag.add_edges_from_list([('S', 'B'), ('B', 'SZ')])
    topo = dag.topological_sort()
    print(f"Topologicznie: {topo}")