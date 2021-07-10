from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        result = set()
        
        for i in range(0,n):
            result.add(i)
            
            
        for edge in edges:
            
            if edge[1] in result:
                result.remove(edge[1])
                
        return list(result)
        