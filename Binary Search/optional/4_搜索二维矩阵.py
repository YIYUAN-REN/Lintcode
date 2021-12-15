# Search a 2D Matrix

"""
等同于搜索1D数组，除了
    length = rows * cols
    r = mid // cols, c = mid % cols
"""

class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = left + (right - left) // 2
            r, c = mid // cols, mid % cols
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False