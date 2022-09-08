# Medium
'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) ==0 or nums[0] >target or nums[-1] < target :
            return [-1,-1]

        start = self.searchStart(nums, target)
        end = self.searchEnd(nums, target)
        return [start,end]
    def searchStart(self,nums,target):
        idx = -1
        l,r = 0,len(nums)-1
        while l <=r:
   
            mid = l + (r-l) // 2
            if nums[mid] == target:
                idx = mid
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                r =mid-1
        return idx
    def searchEnd(self,nums, target):
        idx=-1
        l,r = 0,len(nums)-1
        while l <=r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                idx=mid
                l = mid+1
            elif nums[mid] < target:
                l = mid+1
            else:
                r =mid-1
        return idx
