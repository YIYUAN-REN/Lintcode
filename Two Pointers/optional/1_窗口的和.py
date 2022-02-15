# Window Sum

"""
思路：静态滑动窗口，每次计算减头加尾
"""

class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        if not nums:
            return []

        total = sum(nums[:k])
        results = [total]
        slow, fast = 0, k - 1

        while fast < len(nums) - 1:
            total = total - nums[slow] + nums[fast + 1]
            results.append(total)
            slow += 1
            fast += 1

        return results