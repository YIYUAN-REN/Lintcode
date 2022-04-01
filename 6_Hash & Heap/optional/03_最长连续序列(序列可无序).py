# Longest Consecutive Sequence

"""
思路：建hashset。循环每个num, 若hashset不存在num-1 (即连续序列中的最小数字), 则从该num开始往上找连续数字

Time O(n)
"""

class Solution:
    """
    @param nums: A list of integers
    @return: An integer
    """
    def longest_consecutive(self, nums):
        # write your code here
        max_len, nums_set = 0, set(nums)
        for num in nums:
            if num - 1 not in nums_set:
                low, high = num, num + 1
                while high in nums_set:
                    high += 1
                max_len = max(max_len, high - low)
        return max_len