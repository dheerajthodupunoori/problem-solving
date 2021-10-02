# https://leetcode.com/discuss/interview-question/992306/Indeed-or-Karat-(Phone-Screen)-or-Find-Embedded-Words-I-II

# After catching your classroom students cheating before, you realize your students are getting craftier and hiding
# words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either
# immediately below or immediately to the right of the previous letter.
#
# Given a grid and a word, write a function that returns the location of the word in the grid as a list of
# coordinates. If there are multiple matches, return any one.
#
# grid1 = [
# 	['c', 'c', 'c', 'a', 'r', 's'],
# 	['c', 'c', 'i', 't', 'n', 'b'],
# 	['a', 'c', 'n', 'n', 't', 'i'],
# 	['t', 'c', 'i', 'i', 'p', 't']
# ]
#
# word1_1 = "catnip"
# find_word_location(grid1, word1_1)-> [ (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4) ]
#
# word1_2 = "cccc"
# find_word_location(grid1, word1_2)-> [(0, 1), (1, 1), (2, 1), (3, 1)]
# OR [(0, 0), (1, 0), (1, 1), (2, 1)]
# OR [(0, 0), (0, 1), (1, 1), (2, 1)]
# OR [(1, 0), (1, 1), (2, 1), (3, 1)]
#
#
# grid2 = [
#     ['c', 'p', 'a', 'n', 't', 's'],
#     ['a', 'b', 'i', 't', 'a', 'b'],
#     ['t', 'f', 'n', 'n', 'c', 'i'],
#     ['x', 's', 'c', 'a', 't', 'n'],
#     ['x', 's', 'd', 'd', 'e', 'a'],
#     ['s', 'q', 'w', 'x', 's', 'p']
# ]
#
#
# word2 = "catnap"
# find_word_location(grid2, word2)-> [ (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5) ]
#
# grid3 = [
#     ['c', 'r', 'c', 'a', 'r', 's'],
#     ['a', 'b', 'i', 't', 'n', 'i'],
#     ['t', 'f', 'n', 'n', 'x', 'p'],
#     ['x', 's', 'i', 'x', 'p', 't']
# ]
# word3 = "catnip"
# find_word_location(grid3, word3)-> [ (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5) ]
#
# grid4 = [
#     ['a', 'o', 'o', 'o', 'a', 'a'],
#     ['b', 'b', 'i', 't', 'n', 'i'],
#     ['c', 'f', 'n', 'n', 'v', 'p'],
#     ['o', 'a', 'a', 'a', 'o', 'o']
# ]
# word4_1 = "aaa"
# word4_2 = "ooo"
#
# find_word_location(grid4, word4_1)-> [ (3, 1), (3, 2), (3, 3) ]
# find_word_location(grid4, word4_2)-> [ (0, 1), (0, 2), (0, 3) ]


def find_word_location(grid, word):
    rows = len(grid)
    columns = len(grid[0])
    word_length = len(word)

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == word[0]:
                path = [[i, j]]
                dfs(grid, i, j, rows, columns, word, word_length, 0, path)


def dfs(grid, i, j, rows, columns, word, word_length, current_index, path):
    if current_index == word_length:
        return

    if current_index == word_length - 1:
        print(word, path)
        return

    ix = i + 1
    jy = j

    if is_valid_cell(rows, columns, ix, jy) and grid[ix][jy] == word[current_index + 1]:
        path.append([ix, jy])
        dfs(grid, ix, jy, rows, columns, word, word_length, current_index + 1, path)
        path.pop()

    ix = i
    jy = j + 1

    if is_valid_cell(rows, columns, ix, jy) and grid[ix][jy] == word[current_index + 1]:
        path.append([ix, jy])
        dfs(grid, ix, jy, rows, columns, word, word_length, current_index + 1, path)
        path.pop()


def is_valid_cell(rows, columns, i, j):
    if 0 <= i < rows and 0 <= j < columns:
        return True
    return False


grid1 = [
    ['c', 'c', 'c', 'a', 'r', 's'],
    ['c', 'c', 'i', 't', 'n', 'b'],
    ['a', 'c', 'n', 'n', 't', 'i'],
    ['t', 'c', 'i', 'i', 'p', 't']
]

word1_1 = "catnip"
word1_2 = "cccc"
find_word_location(grid1, word1_1)  # -> [ (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid1, word1_2)  # -> [(0, 1), (1, 1), (2, 1), (3, 1)]
# OR [(0, 0), (1, 0), (1, 1), (2, 1)]
# OR [(0, 0), (0, 1), (1, 1), (2, 1)]
# OR [(1, 0), (1, 1), (2, 1), (3, 1)]
grid2 = [
    ['c', 'p', 'a', 'n', 't', 's'],
    ['a', 'b', 'i', 't', 'a', 'b'],
    ['t', 'f', 'n', 'n', 'c', 'i'],
    ['x', 's', 'c', 'a', 't', 'n'],
    ['x', 's', 'd', 'd', 'e', 'a'],
    ['s', 'q', 'w', 'x', 's', 'p']
]
word2 = "catnap"
find_word_location(grid2, word2)  # -> [ (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (5, 5) ]

grid3 = [
    ['c', 'r', 'c', 'a', 'r', 's'],
    ['a', 'b', 'i', 't', 'n', 'i'],
    ['t', 'f', 'n', 'n', 'x', 'p'],
    ['x', 's', 'i', 'x', 'p', 't']
]
word3 = "catnip"
find_word_location(grid3, word3)  # -> [ (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (2, 5) ]

grid4 = [
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['b', 'b', 'i', 't', 'n', 'i'],
    ['c', 'f', 'n', 'n', 'v', 'p'],
    ['o', 'a', 'a', 'a', 'o', 'o']
]
word4_1 = "aaa"
word4_2 = "ooo"

find_word_location(grid4, word4_1)  # -> [ (3, 1), (3, 2), (3, 3) ]
find_word_location(grid4, word4_2)  # -> [ (0, 1), (0, 2), (0, 3) ]
