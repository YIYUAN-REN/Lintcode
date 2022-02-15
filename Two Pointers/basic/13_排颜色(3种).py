# Sort Colors

"""
思路：[0, left)为0，[left, cursor)为1，[cursor, right]未知，(right, 最后]为2
    若cursor=0，与left交换，cursor前进 (cursor前进因为left一定是1，不能不前进因为left可能超过cursor)
    若cursor=1，cursor前进
    若cursor=2，与right交换 (cursor不前进因为rigth可能是0或1)
"""

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        left, cursor, right = 0, 0, len(nums) - 1
        while cursor <= right:
            if nums[cursor] == 0:
                nums[cursor], nums[left] = nums[left], nums[cursor] # 交换前 left = 1
                left += 1
                cursor += 1
            elif nums[cursor] == 1:
                cursor += 1
            else:
                nums[cursor], nums[right] = nums[right], nums[cursor]   # 交换前 right = 0 or 1
                right -= 1