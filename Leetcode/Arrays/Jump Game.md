https://leetcode.com/problems/jump-game/


----------


**Language:Python**


        class Solution:
            def canJump(self, nums: List[int]) -> bool:
                
                maximum = nums[0]
                steps = nums[0]
                length = len(nums)
                
                if nums[0] == 0 and length > 1:
                    return False
                elif nums[0] == 0:
                    return True
                
                
                for i in range(1,length):
                    
                    if nums[i] == 0 and steps == 1 and maximum <= i and i!=length-1:
                        return False
                    maximum = max(maximum , i+nums[i])
                    if maximum >= length:
                        return True
                    steps -= 1
                    if steps == 0:
                        steps = maximum - i
                    elif steps<0:
                        return False
                return True
                        
                
        