#  Find K Closest Elements

"""
思路：二分法
1. 找到最近的left和right
2. 中心开花，谁小移谁
"""

class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or len(A) == 0:
            return []
        
        left, right = 0, len(A) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] == target:
                right = mid
            elif A[mid] < target:
                left = mid
            else:
                right = mid
        
        results = []
        for _ in range(k):
            if left < 0:
                results.append(A[right])
                right += 1
            elif right == len(A):
                results.append(A[left])
                left -= 1
            elif abs(A[left] - target) <= abs(A[right] - target):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1

        return results