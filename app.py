import streamlit as st
import matplotlib.pyplot as plt
import time
from maze import generate_maze
from astar import astar
from draw import draw_maze

st.set_page_config(page_title="A* Maze Visualizer", layout="centered")
st.title("A* Pathfinding – Step by Step")

size = 6

if st.button("Generate Maze"):
    st.session_state.maze = generate_maze(size)

if "maze" in st.session_state:
    maze = st.session_state.maze

    explored, path = astar(maze, size)

    placeholder = st.empty()   # important

    fig, ax = plt.subplots(figsize=(6, 6), facecolor="black")
    draw_maze(ax, maze, size)

    # Draw START (green)
    ax.scatter(
        0.5,
        size - 0.5,
        color="green",
        s=120,
        label="Start"
    )

    # Draw GOAL (red)
    ax.scatter(
        size - 0.5,
        0.5,
        color="red",
        s=120,
        label="Goal"
    )

    # Animate explored nodes
    for cell in explored:
        # Don't overwrite Start or Goal
        if cell != (0, 0) and cell != (size - 1, size - 1):
            ax.scatter(
                cell[1] + 0.5,
                size - cell[0] - 0.5,
                color="#00bfff",  # blue
                s=40
            )
            placeholder.pyplot(fig)
            time.sleep(0.05)


    # Draw final optimal path
    for cell in path:
        ax.scatter(
            cell[1] + 0.5,
            size - cell[0] - 0.5,
            color="yellow",
            s=90
        )
    ax.legend(loc="upper right", fontsize=8)
    placeholder.pyplot(fig)
    st.success(f"A* Path Length: {len(path)}")
