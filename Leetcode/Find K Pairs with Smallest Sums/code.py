import heapq
from typing import List

class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        result = []
        heap = []
        l1=len(nums1)
        l2=len(nums2)
        visited = set()
        
        heapq.heappush(heap,(nums1[0]+nums2[0],0,0))
        visited.add((0,0))
        
        while k>0:
            
            s,i,j = heapq.heappop(heap)
            
            print(s,i,j)
            
            result.append([nums1[i],nums2[j]])
            
            if i+1 == l1 and j+1==l2:
                break
            
            if j+1<l2 and (i,j+1) not in visited:
            
                heapq.heappush(heap,(nums1[i]+nums2[j+1],i,j+1))
                visited.add((i,j+1))
                
            if i+1<l1 and (i+1,j) not in visited:
                heapq.heappush(heap,(nums1[i+1]+nums2[j],i+1,j))
                visited.add((i+1,j))
                
            k-=1
            
        return result
        