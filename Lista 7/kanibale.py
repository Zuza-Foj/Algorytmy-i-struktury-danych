from graph import Graph

def reconstruct_path(predecessors, target):
    path = []
    curr = target
    while curr is not None:
        path.append(curr)
        curr = predecessors[curr]
    return path[::-1]

def solve_kanibale_i_misionarze():
    g = Graph()
    start = (3, 3, 'L')
    goal = (0, 0, 'R')
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def is_valid(m, k):
        if m < 0 or m > 3 or k < 0 or k > 3: return False
        if m > 0 and m < k: return False
        if 3 - m > 0 and (3 - m) < (3 - k): return False
        return True

    queue = [start]
    visited = {start}
    while queue:
        m, k, boat = queue.pop(0)
        for dm, dk in moves:
            if boat == 'L':
                new_state = (m - dm, k - dk, 'R')
            else:
                new_state = (m + dm, k + dk, 'L')
            if is_valid(new_state[0], new_state[1]):
                g.add_edge((m, k, boat), new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append(new_state)

    distances, predecessors = g.shortest_paths_bfs(start)
    return reconstruct_path(predecessors, goal)

print(solve_kanibale_i_misionarze())
