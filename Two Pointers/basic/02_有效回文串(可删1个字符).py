# Valid Palindrome II

"""
思路：3种情况 (不需删除，删除1次left，删除1次right)，任意一种成功就行
"""

class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        left, right = self.helper(0, len(s) - 1, s)
        if left >= right:
            return True
        
        # 需要删除字符
        left_1, right_1 = self.helper(left + 1, right, s)
        left_2, right_2 = self.helper(left, right - 1, s)
        return left_1 >= right_1 or left_2 >= right_2

    def helper(self, left, right, s):
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1
        return left, right