from graph import Graph
from kanibale import reconstruct_path

def solve_water_jugs():
    g = Graph()
    start = (0, 0)
    queue = [start]
    visited = {start}
    while queue:
        c3, c4 = queue.pop(0)
        if c3 == 2 or c4 == 2:
            goal = (c3, c4)
    states = [(3, c4), (c3, 4), (0, c4), (c3, 0), (max(0, c3-(4-c4)), min(4, c4+c3)), (min(3, c3+c4), max(0, c4-(3-c3)))]
    for state in states:
        g.add_edge((c3, c4), state)
        if state not in visited:
            visited.add(state)
            queue.append(state)

    distances, predecessors = g.shortest_paths_bfs(state)
    for s in distances:
        if s[0] == 2 or s[1] == 2:
            return reconstruct_path(predecessors, s)

print(solve_water_jugs())

