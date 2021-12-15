# Total Occurrence of Target

"""
思路：二分法，找第一次出现和最后一次出现的位置
"""

class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        if not A:
            return 0
        
        # find first
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
            first = left
        elif A[right] == target:
            first = right
        else:
            return 0
        
        # find last
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
            last = right
        elif A[left] == target:
            last = left
        else:
            return 0
        
        return last - first + 1
        