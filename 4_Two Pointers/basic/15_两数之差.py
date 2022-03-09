# Two Sum - Difference equals to target

"""
思路：同向双指针
一直移动fast元素，保持fast元素-slow元素>= target
若差=target，返回
若差!=target，slow前进，fast前进直到差>=target
"""

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        nums.sort()

        fast = 1
        for i in range(len(nums)):
            slow, fast = i, max(fast, i + 1)

            # 将fast移动到 nums[fast]-nums[slow]>=target 的位置
            while fast < len(nums) and nums[fast] - nums[slow] < abs(target):
                fast += 1
            if fast == len(nums):
                break

            # 如果==，则返回。如果>，则继续移动slow
            if nums[fast] - nums[slow] == abs(target):
                return [nums[slow], nums[fast]]
        
        return [-1, -1]