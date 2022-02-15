# Sort Integers II

"""
思路：2挡板3区域:____left____right____
left左侧(不包含left) < pivot, right右侧(不包含right) >= pivot，中间为未知区域

递归
1. base case: 若只有1个/0个元素，终止
2. recursive rule:
    1. partition(把pivot元素放到最后, left到第一个>=pivot，right到第一个<pivot，交换，最后把pivot元素恢复原位)
    2. 左右分别排序
"""

import random

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.quick_sort(0, len(A) - 1, A)
    
    
    def quick_sort(self, start, end, A):
        # 若上轮pivot是最小/最大值，则左半/右半为空，可能上轮start > pivot-1 / pivot+1 > end
        if start >= end:
            return
        pivot_pos = self.partition(start, end, A)
        self.quick_sort(start, pivot_pos - 1, A)
        self.quick_sort(pivot_pos + 1, end, A)
    
    
    def partition(self, start, end, A):
        pivot_pos = random.randint(start, end)
        pivot = A[pivot_pos]
        A[pivot_pos], A[end] = A[end], A[pivot_pos]
        
        left, right = start, end - 1
        while left <= right:
            if A[left] < pivot:		# 根据定义不同，也可以<=pivot
                left += 1
            elif A[right] >= pivot:		# 根据定义不同，也可以>pivot
                right -= 1
            else:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        A[right + 1], A[end] = A[end], A[right + 1]
        
        return right + 1
                