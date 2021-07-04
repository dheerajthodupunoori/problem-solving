from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        
        length = len(height)
        
        if length == 0:
            return 0
        
        left_max = []
        right_max = [0]*(length-1)
        left_max.append(height[0])
        right_max.append(height[length-1])
        result = 0
        for i in range(1,length):
            left_max.append(max(left_max[i-1],height[i]))
            
        print(left_max)
        
        for i in range(length-2,0,-1):
            right_max[i] = max(right_max[i+1],height[i])
            
        print(right_max)
        
        for i in range(1,length-1):
            print(i,min(left_max[i],right_max[i]),height[i])
            result += abs(min(left_max[i],right_max[i]) - height[i])
            print(result)
        
        return result