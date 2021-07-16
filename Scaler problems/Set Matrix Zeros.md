Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.

    > Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.



**Input Format:**

    The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.

**Output Format:**

    Return a 2-d matrix that satisfies the given conditions.

**Constraints:**

    1 <= N, M <= 1000
    0 <= A[i][j] <= 1

**Examples:**

        Input 1:
            [   [1, 0, 1],
                [1, 1, 1], 
                [1, 1, 1]   ]

        Output 1:
            [   [0, 0, 0],
                [1, 0, 1],
                [1, 0, 1]   ]

        Input 2:
            [   [1, 0, 1],
                [1, 1, 1],
                [1, 0, 1]   ]

        Output 2:
            [   [0, 0, 0],
                [1, 0, 1],
                [0, 0, 0]   ]

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
                
                
                