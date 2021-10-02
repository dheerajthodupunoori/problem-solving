# https://leetcode.com/discuss/interview-question/1063081/Indeed-or-Karat-(Video-Screen)-or-Find-Rectangles

# Multiple rectangles. Given a 2D array of 0s and 1s, return a list of the postions of all rectangles made up of 1s.
# Note: you are not allowed to change the input matrix.

# Example 1 input
grid1 = [[0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 1, 0],
         [0, 1, 0, 1, 1, 1, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 1, 0, 0],
         [1, 0, 0, 0, 0, 0, 0]]

#
# # return list of (start_row, start_col, end_row, end_col)
# # for each rectangle:
#  [ (0, 6, 0, 6),
#    (2, 0, 2, 0),
#    (2, 3, 3, 5),
#    (3, 1, 5, 1),
#    (5, 3, 6, 4),
#    (7, 0, 7, 0) ]


grid2 = [[1]]
# # you should return [ (0,0,0,0) ]
#
grid3 = [[0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0]]


# # you should return [ (1, 1, 3, 3) ]


def find_multiple_rectangle_positions(grid):
    rows = len(grid)
    columns = len(grid[0])
    result = []

    visited = [[False for j in range(columns)] for i in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                start_row = i
                start_column = j
                end_row, end_column = dfs(grid, i, j, visited, rows, columns)
                result.append([start_row, start_column, end_row, end_column])

    print(result)


def dfs(grid, i, j, visited, row_length, col_length):
    stack = [(i, j)]
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    end_row = i
    end_col = j

    while stack:
        row, column = stack.pop()

        for x, y in directions:
            new_x = x + row
            new_y = y + column

            if is_valid_cell(row_length, col_length, new_x,new_y) and grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                stack.append((new_x, new_y))
                end_row = max(end_row, new_x)
                end_col = max(end_col, new_y)
                visited[new_x][new_y] = True

    return end_row, end_col


def is_valid_cell(rows, columns, row, column):
    if 0 <= row < rows and 0 <= column < columns:
        return True
    return False


find_multiple_rectangle_positions(grid1)
find_multiple_rectangle_positions(grid2)
find_multiple_rectangle_positions(grid3)
