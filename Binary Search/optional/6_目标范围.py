# Search in a Sorted Array of Unknown Size

"""
思路：找第一个+找最后一个
"""

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
            
        first = self.find_first(A, target)
        last = self.find_last(A, target)
        return [first, last]
    
    
    def find_first(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                right = mid
            elif A[mid] < target:
                left = mid
            else:
                right = mid
        
        if A[left] == target:
            return left
        elif A[right] == target:
            return right
        else:
            return -1
    
    
    def find_last(self, A, target):
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                left = mid
            elif A[mid] < target:
                left = mid
            else:
                right = mid
        
        if A[right] == target:
            return right
        elif A[left] == target:
            return left
        else:
            return -1