# Sort Integers II

"""
思路：递归
1. base case: 只有一个元素时，终止
2. recursive rule: 左半部分排序，右半部分排序，再合并
"""

class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return
        
        self.merge_sort(0, len(A)-1, A, [0 for _ in range(len(A))])
    
    
    def merge_sort(self, start, end, A, temp):
        # 如果只剩一个元素，终止
        if start == end:
            return
        
        mid = start + (end - start) // 2
        self.merge_sort(start, mid, A, temp)
        self.merge_sort(mid+1, end, A, temp)
        self.merge(start, mid, end, A, temp)
    
    
    def merge(self, start, mid, end, A, temp):
        left, right = start, mid+1
        index = start
        
        # loop to put elements into temp
        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right]
                right += 1
            index += 1
            
        # loop to put left remaining elements into temp
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
        
        # loop to put right remaining elements into temp
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
        
        # put temp into original A
        for index in range(start, end+1):
            A[index] = temp[index]