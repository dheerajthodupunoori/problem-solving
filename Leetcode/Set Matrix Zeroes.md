https://leetcode.com/problems/set-matrix-zeroes/

**Approach**
    
        >Create two sets row and columns which tracks the rows and columns at which 0 is present.
        >Traverse the given matrix and where ever you find "0" , add that row position to row set and column position to col set.
        >Now for each row , make that entire row as "0" . And similar to each column as well

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
                
                
                
