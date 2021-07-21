https://leetcode.com/problems/transpose-matrix/


**Language:Python**


    class Solution:
        def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
            
            rows = len(matrix)
            cols = len(matrix[0])
            
            newMatrix = [[0 for j in range(rows)] for i in range(cols)]
            
            for i in range(0,cols):
                for j in range(0,rows):
                    
                    newMatrix[i][j] = matrix[j][i]
                    
            return newMatrix