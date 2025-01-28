# Graph Traversal Algorithms

This project implements graph traversal algorithms to find the shortest path with the least cost between stations in a transportation network. The algorithms used are:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **A-star**

## Project Structure

The project is organized into the following folders:

- **`graph/`**: Contains the main logic and execution of the program.
  - **`main.py`**: The main entry point of the application.
    
  - **`Algorithm/`**: Contains the graph traversal algorithms.
    - **`BFS.py`**: Implements the Breadth-First Search algorithm.
    - **`DFS.py`**: Implements the Depth-First Search algorithm.
    - **`Astar.py`**: Implements the A* algorithm for shortest path finding.

  - **`Resources/`**: Contains the supporting files and data.
    - **`Padre.py`**: Contains common elements shared between the graphs.
    - **`Menu.py`**: Provides an interface to interact with the program.
    - **`Stations.py`**: A dictionary containing station data used for pathfinding.


## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/JaimePerdigueroAlonso/Graph-traversal-algorithm.git
   ```

2. Navigate to the project directory:
   
   ```bash
   cd graph-traversal
   ```

3. Run the main.py
   
   ```bash
   python graph/main.py
   ```
