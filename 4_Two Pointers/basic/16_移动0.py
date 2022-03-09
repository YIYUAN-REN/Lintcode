# Move Zeroes

"""
思路: 同向双指针
若fast元素 == 0，则fast前进
若fast元素 != 0，则slow元素覆盖为fast元素，slow前进，fast前进
"""

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
