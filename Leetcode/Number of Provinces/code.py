from queue import deque
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        
        no_of_cities = len(isConnected)
        
        graph = dict()
        
        visited = [False]*no_of_cities
        
        print(visited)
        
        no_of_provinces = 0
        
        for city in range(0,no_of_cities):
            
            if not visited[city]:
                
                no_of_provinces += 1
                
                self.bfs(isConnected,visited,city,no_of_cities)
                
                
        return no_of_provinces
            
            
    def bfs(self,graph,visited,city,length):
        
        queue = deque()
        
        queue.append(city)
        
        visited[city] = True
        
        while len(queue) > 0:
            
            visited_city = queue.popleft()
            
            for i in range(0,length):
                
                if i!=visited_city and not visited[i] and graph[visited_city][i] != 0:
                    
                    queue.append(i)
                    visited[i] = True  