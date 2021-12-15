# Closest Number in Sorted Array

class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if len(A) == 0:
            return -1
        
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                left = mid
            else:
                right = mid
        
        if abs(A[left] - target) <= abs(A[right] - target):
            return left
        return right