# A* Maze Pathfinding Visualizer

An interactive web application that visually demonstrates the **A*** pathfinding algorithm step by step.
The project is designed as a **learning and visualization tool** to help users understand how heuristic-based search algorithms explore paths and find optimal solutions.

## 🚀 Live Demo

[https://maze-visualizer.streamlit.app/](https://maze-visualizer.streamlit.app/)

## 🧠 About the Project

This application generates a **perfect 6×6 maze** (guaranteed solvable) and visually shows:

* How the A* algorithm explores possible paths
* Which nodes are expanded during the search
* The final optimal path from start to destination

The visualization closely resembles traditional maze-solving tools (like pyamaze), but is implemented as a **web-based application**.

## ✨ Features

* Generates a **random but always solvable maze**
* Step-by-step visualization of the A* algorithm
* Clearly distinguishes:

  * 🟢 Start node
  * 🔴 Goal node
  * 🔵 Explored nodes
  * 🟨 Optimal path
* Displays the length of the optimal path
* Clean and minimal UI for easy understanding

## 🧰 Tech Stack

* **Python**
* **Streamlit** (Web framework)
* **Matplotlib** (Visualization)
* **Heap-based Priority Queue** (A* implementation)

## 📂 Project Structure

```
astar-maze-visualizer/
│── app.py        # Streamlit application
│── maze.py       # Maze generation (recursive backtracking)
│── astar.py      # A* pathfinding algorithm
│── draw.py       # Maze and path rendering logic
│── requirements.txt
```

## ▶️ How to Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run app.py
```

3. Open the browser at:

```
http://localhost:8501
```

##  Algorithm Details

* **g(n):** Cost from the start node to the current node
* **h(n):** Manhattan distance heuristic (admissible)
* **f(n) = g(n) + h(n):** Priority function
* A priority queue ensures the most promising node is explored first
* Guarantees the **optimal shortest path**

##  Learning Outcomes

* Strong understanding of the A* pathfinding algorithm
* Practical use of heuristics and priority queues
* Maze generation using recursive backtracking
* Visualization of algorithm behavior step by step
* Deploying interactive Python applications to the cloud

##  Author

**Shaik Alima Zabi**
GitHub: [https://github.com/shaikalimazabi](https://github.com/shaikalimazabi)
