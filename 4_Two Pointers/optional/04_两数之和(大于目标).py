# Two Sum - Greater than target

"""
思路：right逐次往左，left根据right不断往右，找到第一个和>target的位置
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                count += (right - left)
                right -= 1
        
        return count