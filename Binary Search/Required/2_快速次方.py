# Fast Power

"""
题目目的：a^n大到超出表达范围怎么计算a^n%b

递归
1. base case：若n=0，返回1%b
2. recursive：
    若n为偶数，返回(half_result*half_result)%b
    若n为奇数，返回(half_result*half_result*a)%b
"""

class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b
        
        half_result = self.fastPower(a, b, n // 2)
        if n % 2 == 0:
            return (half_result * half_result) % b
        else:
            return (half_result * half_result * a) % b