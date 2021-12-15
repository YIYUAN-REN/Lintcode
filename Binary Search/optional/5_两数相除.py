# Divide Two Integers

"""
思路：倍增思想，divisor每次乘2
"""

INT_MAX = 2147483647
INT_MIN = -2147483648

class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend, divisor):
        # write your code here
        if divisor == 0:
            return INT_MAX
            
        negative = True if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0 else False
        
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        for i in range(31, -1, -1):
            if dividend >= (divisor << i):
                dividend -= (divisor << i)
                result += (1 << i)
        
        if negative:
            return max(-result, INT_MIN)
        return min(result, INT_MAX)
        