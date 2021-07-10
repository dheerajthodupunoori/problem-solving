from queue import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        no_of_rooms = len(rooms)
        
        result = set()
        
        for i in range(1,no_of_rooms):
            result.add(i)
            
        queue = deque()
        
        queue.append(0)
        
        while len(queue) > 0:
            
            room = queue.popleft()
            
            for key in rooms[room]:
                
                if key in result:
                
                    queue.append(key)
                
                if key in result:
                    
                    result.remove(key)
                
                
        return len(result) == 0
            
            