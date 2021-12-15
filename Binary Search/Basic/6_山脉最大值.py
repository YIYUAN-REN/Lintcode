# Maximum Number in Mountain Sequence

"""
思路：二分法，收拢 比较mid和mid+1, 即判断当前mid位置上升/下降 (如果不用收拢而是判断mid位置是否为山峰，则边界会很麻烦 且 难处理纯上升/下降山脉)
"""

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        
        return max(nums[left], nums[right])