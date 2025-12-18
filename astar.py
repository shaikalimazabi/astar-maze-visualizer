import heapq

def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(maze, size):
    start = (0, 0)
    goal = (size-1, size-1)

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g = {start: 0}
    explored = []

    while open_set:
        _, current = heapq.heappop(open_set)
        explored.append(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return explored, path[::-1]

        for d, (dr, dc) in {
            "N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "W": (0, -1)
        }.items():
            if not maze[current][d]:
                nr, nc = current[0]+dr, current[1]+dc
                nxt = (nr, nc)
                if nxt not in g or g[current]+1 < g[nxt]:
                    g[nxt] = g[current]+1
                    f = g[nxt] + h(nxt, goal)
                    heapq.heappush(open_set, (f, nxt))
                    came_from[nxt] = current

    return explored, []
