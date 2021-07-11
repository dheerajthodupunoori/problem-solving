from queue import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = [False]*numCourses
        rec = [False]*numCourses
        
        graph = dict()
        
        for req in prerequisites:
            
            if req[0] not in graph:
                
                graph[req[0]] = []
                
            graph[req[0]].append(req[1])
        
        print(visited,graph)
        
        for i in range(0,numCourses):
            
            if not visited[i] and i in graph:
                
                result = self.dfs(graph,visited,rec,i)
                
                if result:
                    return False
                
        return True
        
    def dfs(self,graph,visited,rec,course):
        
        visited[course] = True
        rec[course] = True
        
        
        if course in graph:
            
            for adjacent in graph[course]:
                
                if not visited[adjacent]:
                    
                    if self.dfs(graph,visited,rec,adjacent):
                        return True
                    
                elif rec[adjacent]:
                    return True
                
        rec[course] = False
        return False
