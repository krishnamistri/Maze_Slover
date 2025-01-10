1. Initialization
The MazeSolver is initialized with the maze, start position (0, 0), and end position (2, 3).
Directions represent possible moves: down (1, 0), up (-1, 0), right (0, 1), and left (0, -1).
2. BFS Explanation
Step-by-Step Execution:
Initialization:

Queue starts with [(0, 0)] (start position).
Visited nodes: {(0, 0)}.
Parent map tracks the previous node for path reconstruction.
Iteration 1:

Dequeue (0, 0).
Explore its neighbors: (1, 0) (down), (-1, 0) (up), (0, 1) (right), (0, -1) (left).
Valid neighbor: (0, 1). Add to the queue and mark as visited.
Iteration 2:

Dequeue (0, 1).
Explore neighbors: (1, 1), (-1, 1), (0, 2), (0, 0).
Valid neighbor: (0, 2).
Iteration 3:

Dequeue (0, 2).
Explore neighbors: (1, 2), (-1, 2), (0, 3), (0, 1).
Valid neighbors: (1, 2).
Iteration 4:

Dequeue (1, 2).
Explore neighbors: (2, 2), (0, 2), (1, 3), (1, 1).
Valid neighbors: (2, 2).
Iteration 5:

Dequeue (2, 2).
Explore neighbors: (3, 2), (1, 2), (2, 3), (2, 1).
Valid neighbor: (2, 3) (end node). Stop the search.
Reconstruct Path:
Using the parent_map, trace back from (2, 3) to (0, 0):

makefile
Copy code
Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)]
3. DFS Explanation
Step-by-Step Execution:
Initialization:

Stack starts with [(0, 0)] (start position).
Visited nodes: set().
Parent map tracks the previous node for path reconstruction.
Iteration 1:

Pop (0, 0).
Explore neighbors: (1, 0), (-1, 0), (0, 1), (0, -1).
Valid neighbor: (0, 1). Add to the stack.
Iteration 2:

Pop (0, 1).
Explore neighbors: (1, 1), (-1, 1), (0, 2), (0, 0).
Valid neighbor: (0, 2).
Iteration 3:

Pop (0, 2).
Explore neighbors: (1, 2), (-1, 2), (0, 3), (0, 1).
Valid neighbor: (1, 2).
Iteration 4:

Pop (1, 2).
Explore neighbors: (2, 2), (0, 2), (1, 3), (1, 1).
Valid neighbor: (2, 2).
Iteration 5:

Pop (2, 2).
Explore neighbors: (3, 2), (1, 2), (2, 3), (2, 1).
Valid neighbor: (2, 3) (end node). Stop the search.
Reconstruct Path:
Using the parent_map, trace back from (2, 3) to (0, 0):

makefile
Copy code
Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3)]
4. BFS vs DFS Visual Representation
I'll generate images that illustrate the exploration process for BFS and DFS.


