# Valid Palindrome II

"""
˼·��3����� (����ɾ����ɾ��1��left��ɾ��1��right)������һ�ֳɹ�����
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
        
        # ��Ҫɾ���ַ�
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