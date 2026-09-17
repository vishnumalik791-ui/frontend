from collections import deque
import matplotlib.pyplot as plt
import numpy as np

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    queue = deque([start])
    visited = set([start])
    parent = {}

    # Up, Down, Left, Right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and
                0 <= ny < cols and
                grid[nx][ny] == 0 and
                (nx, ny) not in visited):

                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return None


def visualize(grid, path, start, goal):
    rows, cols = len(grid), len(grid[0])

    image = np.ones((rows, cols, 3))

    # White = Free cells
    image[:] = [1, 1, 1]

    # Black = Obstacles
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                image[i, j] = [0, 0, 0]

    # Yellow = Path
    if path:
        for x, y in path:
            image[x, y] = [1, 1, 0]

    # Green = Start
    image[start] = [0, 1, 0]

    # Red = Goal
    image[goal] = [1, 0, 0]

    plt.figure(figsize=(6,6))
    plt.imshow(image)

    # Draw grid lines
    plt.xticks(range(cols))
    plt.yticks(range(rows))
    plt.grid(color='gray', linewidth=1)

    # Display coordinates
    for i in range(rows):
        for j in range(cols):
            plt.text(j, i, f"({i},{j})",
                     ha='center', va='center',
                     fontsize=9, color='blue')

    plt.title("Breadth First Search (BFS) - Shortest Path")
    plt.show()


# ---------------- Main ----------------

# 0 = Free cell
# 1 = Obstacle

grid = [
    [0,0,0,1],
    [1,0,0,0],
    [0,0,1,0],
    [0,0,0,0]
]

start = (0,0)
goal = (3,3)

path = bfs(grid, start, goal)

print("Shortest Path:")
print(path)

visualize(grid, path, start, goal)