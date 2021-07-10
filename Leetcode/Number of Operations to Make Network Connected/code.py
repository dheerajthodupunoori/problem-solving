from typing import DefaultDict, List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        
        
        no_of_connections = len(connections)
        
        if no_of_connections < n-1:
            return -1
        
        graph = DefaultDict(list)
        
        result = set()
        totalFound = 0
        
        for u,v in connections:
            
            graph[u].append(v)
            graph[v].append(u)
                
        
        for i in range(0,n):
            
            if i not in result:
                
                totalFound += 1
                
                self.dfs(graph,result,i)
                
                
        return totalFound-1
                
                
    def dfs(self,graph,result,vertex):

        if vertex not in result and vertex in graph:

            result.add(vertex)

            for adjacent_computer in graph[vertex]:

                self.dfs(graph,result,adjacent_computer)