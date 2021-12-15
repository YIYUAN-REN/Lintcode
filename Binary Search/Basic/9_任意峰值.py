# Find Peak Element

"""
思路：二分法，四种情况(上升，下降，峰顶，峰底)
"""

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        left, right = 1, len(A) - 2
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid - 1] < A[mid] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1