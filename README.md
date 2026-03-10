# Graph-lab

Graph Lab is an interactive Streamlit application for graph construction and algorithmic analysis. 
It provides a visual interface for users to draw graphs and execute a wide range of algorithms for pathfinding, connectivity, flow, and matching.

### Key Features:
* Interactive Construction: Draw graphs manually with support for directed and undirected edges.
* Bipartite Support: Toggle bipartite mode to define specific left and right node sets.
* Intelligent Execution: Choose between two distinct operational modes:
* Run Algorithm: Manually select and execute a specific algorithm.
* Run Task: The system analyzes graph properties (such as density or weight types) to select the mathematically optimal algorithm for the task. For example, it automatically switches between Kruskal’s and Prim’s based on whether the graph is sparse or dense.

### Supported algorithms:

#### Bipartite Algorithms:
* Hopcroft-Karp: Maximum cardinality matching.
* Hungarian Algorithm: Minimum/Maximum weight matching for assignment problems.

#### Traversal and Pathfinding:
* BFS & DFS: Breadth-First Search and Depth-First Search (Recursive and Iterative).
* Dijkstra: Shortest path for graphs with non-negative weights.
* Bellman-Ford: Shortest path handling negative edge weights.
* Floyd-Warshall: All-pairs shortest path.
* Johnson’s Algorithm: All-pairs shortest path optimized for sparse graphs.

#### Minimum Spanning Tree (MST):
* Prim’s Algorithm: Optimized for dense graphs.
* Kruskal’s Algorithm: Optimized for sparse graphs.

#### Connectivity and Flow:
* Kosaraju & Tarjan: Identification of strongly connected components.
* Edmonds-Karp: Max-flow using augmenting paths.
* Dinic’s Algorithm: Highly efficient max-flow using level graphs and blocking flows.

## Installation 

Clone the repository:
git clone https://github.com/victoria2011725/Graph-lab
cd Graph-lab 
pip install streamlit networkx matplotlib pandas 
Run the application:
streamlit run app.py
