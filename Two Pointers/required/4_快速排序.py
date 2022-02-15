# Sort Integers II

"""
˼·��2����3����:____left____right____
left���(������left) < pivot, right�Ҳ�(������right) >= pivot���м�Ϊδ֪����

�ݹ�
1. base case: ��ֻ��1��/0��Ԫ�أ���ֹ
2. recursive rule:
    1. partition(��pivotԪ�طŵ����, left����һ��>=pivot��right����һ��<pivot������������pivotԪ�ػָ�ԭλ)
    2. ���ҷֱ�����
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
        # ������pivot����С/���ֵ�������/�Ұ�Ϊ�գ���������start > pivot-1 / pivot+1 > end
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
            if A[left] < pivot:		# ���ݶ��岻ͬ��Ҳ����<=pivot
                left += 1
            elif A[right] >= pivot:		# ���ݶ��岻ͬ��Ҳ����>pivot
                right -= 1
            else:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        A[right + 1], A[end] = A[end], A[right + 1]
        
        return right + 1
                