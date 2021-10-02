# https://leetcode.com/discuss/interview-question/866234/Indeed-telephonic-Interview-Question
# In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
#
# A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
# then one square in an orthogonal direction.
#
# Return the minimum number of steps needed to move the knight to the square [x, y].  It is guaranteed the answer exists
#
# Input: x = 2, y = 1
# Output: 1
# Explanation: [0, 0] → [2, 1]
#
# Input: x = 5, y = 5
# Output: 4
# Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]


from collections import deque


def minimum_moves_by_knight(target):
    start_x = 0
    start_y = 0
    directions = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

    queue = deque()
    queue.append((start_x, start_y, 0))
    visited = set()
    visited.add((start_x, start_y))

    while len(queue) > 0:
        x, y, distance = queue.popleft()
        if x == target[0] and y == target[1]:
            print("Minimum number of moves by knight - ", distance)
            return
        for i in range(8):
            new_x = x + directions[i][0]
            new_y = y + directions[i][1]
            if (new_x, new_y) not in visited:
                queue.append((new_x, new_y, distance + 1))
                visited.add((new_x, new_y))


minimum_moves_by_knight([2, 1])
minimum_moves_by_knight([5, 5])
minimum_moves_by_knight([30, 30])
