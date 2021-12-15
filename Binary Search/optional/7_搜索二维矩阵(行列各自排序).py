# Search a 2D Matrix II

"""
思路：从左下/右上开始。比如右上开始，若比当前小则往左，若比当前大则往下
"""

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix or not matrix[0]:
            return 0
        
        count = 0
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols - 1
        
        while r < rows and c >= 0:
            if matrix[r][c] == target:
                count += 1
                r += 1
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        
        return count