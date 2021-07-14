https://leetcode.com/problems/maximum-of-absolute-value-expression/

**Language:Python**

class Solution:
	def maxAbsValExpr(self, nums1: List[int], nums2: List[int]) -> int:

		length = len(nums1)
		arr1 = [0]*length
		arr2 = [0]*length
		arr3 = [0]*length
		arr4 = [0]*length

		for i in range(length):
			arr1[i] = nums1[i]+nums2[i]+i
			arr2[i] = nums1[i]+nums2[i]-i
			arr3[i] = nums1[i]-nums2[i]+i
			arr4[i] = nums1[i]-nums2[i]-i
			
		return max((max(arr1)-min(arr1)),
					(max(arr2)-min(arr2)),
					(max(arr3)-min(arr3)),
					(max(arr4)-min(arr4)))
