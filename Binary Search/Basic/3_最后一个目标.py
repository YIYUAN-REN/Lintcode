# Last Position of Target

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid     # not right = mid - 1
            elif nums[mid] < target:
                left = mid      # or left = mid + 1
            else:
                right = mid     # or right = mid - 1
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1