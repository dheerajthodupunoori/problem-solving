# Given a position (x, y), return all the immediate neighbor coordinates that can be taken from the position without hitting -1 in all four directions.
#
# For example,
# (0, 0) -> [(0, 1), (1, 0)]
# (4, 0) -> [(5, 0)]
#

#
# grid = [
#     [  0,  0,  0, 0, -1 ],
#     [  0, -1, -1, 0,  0 ],
#     [  0,  0,  0, 0,  0 ],
#     [ -1, -1,  0, 0,  0 ],
#     [  0, -1,  0, 0,  0 ],
#     [  0, -1,  0, 0,  0 ],
# ]

def return_all_immediate_neighbours(grid, position):
    directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    row = len(grid)
    column = len(grid[0])
    result = []

    for direction in directions:
        position_x = position[0] + direction[0]
        position_y = position[1] + direction[1]
        if is_valid_position(grid, [position_x, position_y], row, column) and grid[position_x][position_y] == 0:
            result.append([position_x, position_y])
    print(result)
    return result


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

return_all_immediate_neighbours(input, [0, 0])
return_all_immediate_neighbours(input, [4, 0])
return_all_immediate_neighbours(input, [4, 3])
return_all_immediate_neighbours(input, [5, 4])
