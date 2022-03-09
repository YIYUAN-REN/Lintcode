# Two Sum - Closest to target

"""
思路：趋近target过程中随时更新min diff
"""

class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        min_diff = float('inf')
        left, right = 0, len(nums) - 1
        
        while left < right:
            min_diff = min(min_diff, abs(nums[left] + nums[right] - target))
            
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                right -= 1
        
        return min_diff # 返回与target的最小diff