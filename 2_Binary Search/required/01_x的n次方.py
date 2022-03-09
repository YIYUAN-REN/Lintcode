# Pow(x, n)

"""
递归
1. base case: pow(x, 0) = 1
2. recursive rule: 
    if n是偶数, pow(x, n) = pow(x, n//2) * pow(x, n//2)
    if n是奇数, pow(x, n) = pow(x, n//2) * pow(x, n//2) * x
注意：检查
    分母为0情况
    n为负的情况
"""

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if x == 0 and n <= 0:
            return -1
        elif n < 0:
            return self.pow(1 / x, -n)
        else:
            return self.pow(x, n)
    
    
    def pow(self, x, n):
        if n == 0:
            return 1
        
        half_result = self.pow(x, n // 2)
        if n % 2 == 1:
            return half_result * half_result * x
        else:
            return half_result * half_result