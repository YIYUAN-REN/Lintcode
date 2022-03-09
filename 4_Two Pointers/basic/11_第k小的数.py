# Kth Smallest Numbers in Unsorted Array

"""
思路：快速选择 O(n) + O(n/2) + ... = O(n)
    1. partition
    2. 取左(< pivot)/取右(>= pivot)
"""

import random

class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        self.quick_select(0, len(nums) - 1, nums, k)
        return nums[k - 1]  # 即pivot
    
    
    def quick_select(self, start, end, nums, k):
        if start >= end:
            return
        
        pivot_pos = self.partition(start, end, nums)
        # pivot_pos == k 默认return
        if pivot_pos < k:
            self.quick_select(pivot_pos + 1, end, nums, k)
        elif:
            self.quick_select(start, pivot_pos - 1, nums, k)
    
    
    def partition(self, start, end, nums):
        pivot_pos = random.randint(start, end)
        pivot = nums[pivot_pos]
        nums[pivot_pos], nums[end] = nums[end], nums[pivot_pos]
        
        left, right = start, end - 1
        while left <= right:
            if nums[left] < pivot:
                left += 1
            elif nums[right] >= pivot:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        nums[right + 1], nums[end] = nums[end], nums[right + 1] # 必须换回来, 因为pivot要参与下次quick select
        
        return right + 1