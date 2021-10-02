# https://leetcode.com/discuss/interview-question/1062462/Indeed-Karat-Questions
# https://leetcode.com/discuss/interview-question/1063081/Indeed-or-Karat-(Video-Screen)-or-Find-Rectangles

# Given a 2D array of 0s and 1s, return the position of the single rectangle made up of 1s.
#
# # Example input
grid1 = [[0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]

grid3 = [[0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 0, 0]]


# # you should return the
# # (start_row, start_col, end_row, end_col)
#          [ 1, 1, 2, 3 ]


def get_rectangle_position(grid):
    start_row = 0
    start_col = 0
    end_row = 0
    end_col = 0

    row_length = len(grid)
    col_length = len(grid[0])

    is_one_found = False

    for i in range(row_length):
        for j in range(col_length):
            if grid[i][j] == 1:
                # print(i, j)
                start_row = i
                start_col = j
                is_one_found = True
                break

        if is_one_found:
            break

    # print(start_row, start_col)

    for row in range(start_row, row_length):
        if grid[row][start_col] == 1:
            end_row = row

    for col in range(start_col, col_length):
        if grid[start_row][col] == 1:
            end_col = col

    print(start_row, start_col, end_row, end_col)


get_rectangle_position(grid1)
get_rectangle_position(grid3)
