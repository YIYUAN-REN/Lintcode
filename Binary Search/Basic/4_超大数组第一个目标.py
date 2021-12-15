# Search in a Big Sorted Array

"""
思路：
1. 不断扩大范围找right的位置
2. 二分法
"""

class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        left, right = 0, 1
        while reader.get(right) < target:
            right *= 2
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if reader.get(mid) == target:
                right = mid
            elif reader.get(mid) < target:
                left = mid
            else:
                right = mid
        
        if reader.get(left) == target:
            return left
        elif reader.get(right) == target:
            return right
        return -1