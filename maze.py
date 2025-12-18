import random

def generate_maze(n):
    maze = {}
    visited = set()

    for r in range(n):
        for c in range(n):
            maze[(r, c)] = {"N": True, "S": True, "E": True, "W": True}

    def neighbors(cell):
        r, c = cell
        dirs = []
        if r > 0: dirs.append(("N", (r-1, c)))
        if r < n-1: dirs.append(("S", (r+1, c)))
        if c > 0: dirs.append(("W", (r, c-1)))
        if c < n-1: dirs.append(("E", (r, c+1)))
        random.shuffle(dirs)
        return dirs

    def carve(cell):
        visited.add(cell)
        for d, nxt in neighbors(cell):
            if nxt not in visited:
                maze[cell][d] = False
                if d == "N": maze[nxt]["S"] = False
                if d == "S": maze[nxt]["N"] = False
                if d == "E": maze[nxt]["W"] = False
                if d == "W": maze[nxt]["E"] = False
                carve(nxt)

    # Start carving from START cell
    carve((0, 0))
    return maze
