def draw_maze(ax, maze, size):
    ax.set_facecolor("black")
    ax.set_aspect("equal")   # 🔑 VERY IMPORTANT

    for (r, c), walls in maze.items():
        x = c
        y = size - r - 1

        if walls["N"]:
            ax.plot([x, x+1], [y+1, y+1], color="white", lw=2)
        if walls["S"]:
            ax.plot([x, x+1], [y, y], color="white", lw=2)
        if walls["E"]:
            ax.plot([x+1, x+1], [y, y+1], color="white", lw=2)
        if walls["W"]:
            ax.plot([x, x], [y, y+1], color="white", lw=2)

    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.axis("off")
