https://leetcode.com/problems/partition-array-into-disjoint-intervals/

**Language:Python**


    class Solution:
        def partitionDisjoint(self, nums: List[int]) -> int:
            
            length = len(nums)
            
            maximum = [0]*length
            maximum[0] = nums[0]
            
            minimum = [0]*length
            minimum[length-1] = nums[length-1]
            
            for i in range(1,length):
                
                if nums[i] > maximum[i-1]:
                    
                    maximum[i] = nums[i]
                    
                else:
                    
                    maximum[i] = maximum[i-1]
                    
                    
            print(maximum)
        
            for j in range(length-2,-1,-1):
                
                if nums[j] < minimum[j+1]:
                    minimum[j] = nums[j]
                else:
                    minimum[j] = minimum[j+1]
            
            print(minimum)
            
            for i in range(length-1):
                
                if maximum[i] <= minimum[i+1]:
                    break
                
            return i+1
                
                
            