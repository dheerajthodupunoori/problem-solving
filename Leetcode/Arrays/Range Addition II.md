**Problem statement**

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

***

> **Example 1:**
> **Input:** m = 3, n = 3, ops = [[2,2],[3,3]]
> **Output:** 4
> **Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4.
> ![image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/184sixklw3abox8wsxiz.png)
 
***

> **Example 2:**
> **Input:** m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
> **Output: 4**

***

> **Example 3:**
> **Input:** m = 3, n = 3, ops = []
> **Output:** 9

***

**Constraints:**

* 1 <= m, n <= 4 * 104
* 1 <= ops.length <= 104
* ops[i].length == 2
* 1 <= ai <= m
* 1 <= bi <= n

***

**Idea**
> The problem statement says that we will be given a matrix and an array of matrix cell positions , we need to increment the count of all the cells from (0,0) to each matrix cell position. After completing all these operations we need to find out the count of maximum integer in the matrix.

> So , the question is to find out the count of the maximum integer after performing all the given operations.

> As per the question , a cell **(x , y)** value can be incremented if and only if **(x , y)** is one of the cell from **(0,0)** to the given input **(p , q)**.

> So , the maximum integer will be produced when matrix cell value is incremented more number of times.

> For a matrix cell to be maximum value , we need to figure out the most overlapping cell between the given set of operations/matrix cell positions as the range of cells which overlaps the most will get chance to increment more number of times.

> If you look at the first example , in first operation each cell value is incremented from **(0,0) to (2,2)** , in second operation each cell from **(0,0) to (2,2)** again got incremented as it overlaps with **(3,3)**.

> So , solution is to simple find out the **product of minimum of first co-ordinates of cell and minimum of second co-ordinates of cell**.

> We are taking product because we need to find out the count of the maximum integer in the matrix after performing all the given operations.

***

**Code-Python**

```python
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        length = len(ops)
        if length == 0:
            return m*n
        result = [ops[0][0] , ops[0][1]]
        for i in range(1,length):
            result[0] = min(result[0] , ops[i][0])
            result[1] = min(result[1] , ops[i][1])
        return result[0]*result[1]        
```

***