import heapq

rowDir = [0, 0, 1, -1]
colDir = [1, -1, 0, 0]

class Node:
    def __init__(self, row, col, g, h, parent=None):
        self.row = row
        self.col = col
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f

def heuristic(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def is_valid(row, col, grid):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != '#'

def print_path(node, grid, start, goal):
    while node:
        if (node.row, node.col) != start and (node.row, node.col) != goal:
            grid[node.row][node.col] = 'P'
        node = node.parent

    grid[start[0]][start[1]] = 'S'
    grid[goal[0]][goal[1]] = 'G'

    print("\nLegend:\nS = Start\nG = Goal\nP = Path\n# = Wall\n. = Open cell\n")
    print("Grid with shortest path:\n")
    for i, row in enumerate(grid):
        print(i, ' '.join(row))

def a_star(input_grid, start, goal):
    grid = [list(row) for row in input_grid]
    rows, cols = len(grid), len(grid[0])

    open_list = []
    visited = [[False]*cols for _ in range(rows)]

    start_node = Node(start[0], start[1], 0, heuristic(start[0], start[1], goal[0], goal[1]))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)
        row, col = current.row, current.col

        if visited[row][col]:
            continue
        visited[row][col] = True

        if (row, col) == goal:
            print_path(current, grid, start, goal)
            return

        for i in range(4):
            new_row = row + rowDir[i]
            new_col = col + colDir[i]

            if is_valid(new_row, new_col, grid) and not visited[new_row][new_col]:
                g = current.g + 1
                h = heuristic(new_row, new_col, goal[0], goal[1])
                neighbor = Node(new_row, new_col, g, h, current)
                heapq.heappush(open_list, neighbor)

    print("No path found!")

def main():
    grid = [
        "....#.....",
        "##.##.###.",
        "........#.",
        ".####.#.#.",
        "....#.#...",
        "#.#.#.##.#",
        ".##.#..#..",
        ".....####.",
        ".###......",
        ".....#####"
    ]

    start = (0, 0)
    goal = (8, 9)

    a_star(grid, start, goal)

if __name__ == "__main__":
    main()
