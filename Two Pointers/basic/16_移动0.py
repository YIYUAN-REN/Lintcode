# Move Zeroes

"""
˼·: ͬ��˫ָ��
��fastԪ�� == 0����fastǰ��
��fastԪ�� != 0����slowԪ�ظ���ΪfastԪ�أ�slowǰ����fastǰ��
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
