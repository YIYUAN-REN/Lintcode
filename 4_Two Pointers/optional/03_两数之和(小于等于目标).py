# Two Sum - Less than or equal to target

"""
思路：排序后双指针。left逐次往右，right根据left不断向左，找到第一个和<=target的位置
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] <= target:
                count += (right - left) # 因为这里不是=，需要一次性把满足的结果加入再移动left
                left += 1
            else:
                right -= 1
        
        return count