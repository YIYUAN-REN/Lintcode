# Partition Array

"""
思路：相向双指针
left左侧始终小于k, right右侧始终大于k
"""

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < k:
                left += 1
            elif nums[right] >= k:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return right + 1    # 划分的位置