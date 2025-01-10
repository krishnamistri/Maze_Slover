from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.start = (0, 0)  # Starting position (row, column)
        self.end = (2, 3)    # Ending position (row, column)
        self.DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def is_valid_move(self, visited, position):
        x, y = position
        return (0 <= x < len(self.maze) and 
                0 <= y < len(self.maze[0]) and 
                self.maze[x][y] != '#' and 
                position not in visited)

    def bfs(self):
        queue = deque([self.start])
        visited = set()
        visited.add(self.start)
        parent_map = {self.start: None}

        while queue:
            current = queue.popleft()
            
            if current == self.end:
                return self.reconstruct_path(parent_map)

            for dx, dy in self.DIRECTIONS:
                neighbor = (current[0] + dx, current[1] + dy)
                if self.is_valid_move(visited, neighbor):
                    visited.add(neighbor)
                    parent_map[neighbor] = current
                    queue.append(neighbor)

        return None  # No path found

    def dfs(self):
        stack = [self.start]
        visited = set()
        parent_map = {self.start: None}

        while stack:
            current = stack.pop()

            if current == self.end:
                return self.reconstruct_path(parent_map)

            if current not in visited:
                visited.add(current)

                for dx, dy in self.DIRECTIONS:
                    neighbor = (current[0] + dx, current[1] + dy)
                    if self.is_valid_move(visited, neighbor):
                        parent_map[neighbor] = current
                        stack.append(neighbor)

        return None  # No path found

    def reconstruct_path(self, parent_map):
        path = []
        current = self.end
        while current is not None:
            path.append(current)
            current = parent_map[current]
        return path[::-1]  # Return reversed path

    def print_maze_with_path(self, path):
        for x in range(len(self.maze)):
            for y in range(len(self.maze[0])):
                if (x, y) in path:
                    print('*', end=' ')  # Mark the path with '*'
                else:
                    print(self.maze[x][y], end=' ')
            print()

# Example usage
# Define the maze as a 2D list
MAZE = [
    ['S', '.', '.', '#'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', 'E']
]

solver = MazeSolver(MAZE)

print("Maze:")
for row in MAZE:
    print(" ".join(row))

print("\nBFS Path:")
bfs_path = solver.bfs()
print(bfs_path)

if bfs_path:
    solver.print_maze_with_path(bfs_path)

print("\nDFS Path:")
dfs_path = solver.dfs()
print(dfs_path)

if dfs_path:
    solver.print_maze_with_path(dfs_path)
