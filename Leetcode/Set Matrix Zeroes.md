https://leetcode.com/problems/set-matrix-zeroes/

**Language:Python**

    class Solution:
        def setZeroes(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            rows = set()
            columns = set()

            row = len(matrix)
            col = len(matrix[0])

            for i in range(row):
                for j in range(col):
                    if matrix[i][j] == 0:
                        rows.add(i)
                        columns.add(j)

            for i in rows:
                for j in range(col):
                    matrix[i][j] = 0

            for col in columns:
                for j in range(row):
                    matrix[j][col] = 0
                
                
                
