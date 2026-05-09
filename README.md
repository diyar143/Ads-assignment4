# Assignment 4

## Project Overview
This project implements a directed graph using an **Adjacency List** representation. The system includes two primary traversal algorithms: **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**, with a focus on comparing their execution performance across various graph sizes.

## Class Descriptions
- **Vertex**: Stores a unique identifier (`id`) for each node in the graph.
- **Edge**: Defines a directed connection from a `source` vertex to a `destination` vertex.
- **Graph**: Manages the graph structure using a dictionary-based Adjacency List. It provides methods for adding vertices, establishing edges, and executing traversals.
- **Experiment**: Automates the testing process by generating random graphs of size 10, 30, and 100, measuring performance in nanoseconds.

## Algorithm Descriptions

### Breadth-First Search (BFS)
- **Methodology**: Operates level-by-level using a **Queue**. It visits all immediate neighbors before moving to the next level.
- **Complexity**: $O(V + E)$, where $V$ is vertices and $E$ is edges.
- **Behavior**: Guarantees finding the shortest path in terms of the number of edges in an unweighted graph.

### Depth-First Search (DFS)
- **Methodology**: Uses **Recursion** to explore as far as possible along each branch before backtracking.
- **Complexity**: $O(V + E)$.
- **Behavior**: Highly efficient for exploring all possible paths and detecting cycles within the graph structure.

## Experimental Results
Times measured using `time.perf_counter_ns()`.

<img width="680" height="314" alt="image" src="https://github.com/user-attachments/assets/6e44da5d-bd56-41c8-b38e-72d9e80cb0e9" />


## Analysis
- **Scalability**: Both algorithms exhibit linear growth in execution time relative to the increase in vertices and edges, confirming $O(V + E)$ complexity.
- **Comparison**: In random graph tests, DFS often shows slightly lower overhead due to the direct nature of recursion compared to manual queue management in BFS.
- **Search Patterns**: BFS is better for finding nodes close to the source, whereas DFS is optimal for complete branch exploration.

## Reflection
This project deepened my understanding of non-linear data structures. Implementing the Adjacency List showed how memory-efficient graph storage can be compared to an Adjacency Matrix. The main challenge was managing recursion limits for DFS and ensuring that the BFS queue correctly handled nodes to avoid redundant processing.
