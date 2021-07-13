from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        left = 0
        right = length-1
        
        if length==1:
            return 0
        
        if nums[0]>nums[1]:
            return 0
        
        if nums[right] > nums[right-1]:
            return right
        
        while left < right:
            
            
            mid = (left+right)//2
            
            print(left,right,mid)

            
            if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[mid-1] > nums[mid]:
                right = mid
                
            elif nums[mid+1] > nums[mid]:
                left = mid+1
                
                
        print("outside while loop")
                
        return mid
            
            
        