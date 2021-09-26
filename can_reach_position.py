# Given a position (x, y), return if it is possible to start from any 0 in the grid and reach the position.
#
# For Example,
# (0, 0) -> False since (4, 0) and (5, 0) are blocked by -1 and so cannot reach (0, 0)

# grid = [
#     [  0,  0,  0, 0, -1 ],
#     [  0, -1, -1, 0,  0 ],
#     [  0,  0,  0, 0,  0 ],
#     [ -1, -1,  0, 0,  0 ],
#     [  0, -1,  0, 0,  0 ],
#     [  0, -1,  0, 0,  0 ],
# ]


def can_reach_position(grid, position = None):
    row = len(grid)
    column = len(grid[0])
    visited = []

    for i in range(row):
        new_column = []
        for j in range(column):
            new_column.append(False)
        visited.append(new_column)

    for i in range(row):
        for j in range(column):
            if grid[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                visit_neighbours(grid, i, j, visited, row, column)

    are_all_reached = check_if_all_visited(grid)
    return are_all_reached


def visit_neighbours(grid, row, column, visited, rows, columns):
    visited[row][column] = True
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    stack = [[row, column]]

    while stack:
        row, column = stack.pop()
        for direction in directions:
            px = row + direction[0]
            py = column + direction[1]
            if is_valid_position(grid, [px, py], rows, columns) and grid[px][py] == 0 and not visited[px][py]:
                visited[px][py] = True
                stack.append([px, py])


def check_if_all_visited(grid):
    for row in grid:
        for col in row:
            if not col:
                return False
    return True


def is_valid_position(grid, position, row, column):
    if 0 <= position[0] < row and 0 <= position[1] < column:
        return True
    return False


input = [
    [0, 0, 0, 0, -1],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [-1, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
]

print(can_reach_position(input))

