# Prime Factorization

"""
思路：1) 从小到大枚举质因数  2) 对于每个质因数，num不断整除此数直到不能  3) num剩余最后一个数单独加入
"""

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        if num <= 1:
            return []
        
        results = []
        i = 2
        while i * i <= num:
            while num % i == 0:
                results.append(i)
                num //= i
            i += 1
        
        if num > 1:
            results.append(num)
            
        return results