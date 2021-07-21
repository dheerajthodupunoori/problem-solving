Rotate Matrix

Problem Description

    You are given a n x n 2D matrix A representing an image.

    Rotate the image by 90 degrees (clockwise).

    You need to do this in place.

Note: If you end up using an additional array, you will only receive partial score.



Problem Constraints

    1 <= n <= 1000



Input Format
    First argument is a 2D matrix A of integers



Output Format
    Return the 2D rotated matrix.



Example Input
Input 1:

 [
    [1, 2],
    [3, 4]
 ]
Input 2:

 [
    [1]
 ]


Example Output
Output 1:

 [
    [3, 1],
    [4, 2]
 ]
Output 2:

 [
    [1]
 ]


Example Explanation
Explanation 1:

 After rotating the matrix by 90 degree:
 1 goes to 2, 2 goes to 4
 4 goes to 3, 3 goes to 1
Explanation 2:

 2D array remains the ssame as there is only element.



 **Language:Python**

        class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            """
            Do not return anything, modify matrix in-place instead.
            """
            for i in range(0,len(matrix)):
                for j in range(i+1,len(matrix[0])):
                    matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                    
            for lst in matrix:
                lst.reverse()
             
            