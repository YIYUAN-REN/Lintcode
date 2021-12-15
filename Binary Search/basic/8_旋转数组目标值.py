# Search in Rotated Sorted Array

"""
思路：二分法，跟找最小一样，但收拢到哪边要额外判断target在哪一段
"""

class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        left, right = 0, len(A) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                return mid
            elif A[mid] < A[right]:
                if A[mid] < target <= A[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if A[left] <= target < A[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1