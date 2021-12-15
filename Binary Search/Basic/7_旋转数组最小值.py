# Find Minimum in Rotated Sorted Array

"""
思路：二分法，收拢 比较mid和right, 即判断当前mid在哪一半上升数组
"""

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid
        
        return min(nums[left], nums[right])