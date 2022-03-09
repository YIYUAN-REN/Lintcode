# Factor Combinations

"""
硬币组合变种，把加法改成乘法
1. 找到所有factors
2. 把factors作为"硬币币值"，进行dfs(加法变乘法)
"""

class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        factors = []
        for factor in range(2, n // 2 + 1):
            if n % factor == 0:
                factors.append(factor)
        
        results = []
        self.dfs(0, n, factors, [], results)
        return results
    
    
    def dfs(self, index, remain, factors, combination, results):
        if remain == 1:
            results.append(list(combination))
            return
        
        if index == len(factors):
            return
        
        # 加0个factor的情况
        self.dfs(index + 1, remain, factors, combination, results)

        # 加1至n个factor的情况
        size = len(combination)
        while remain % factors[index] == 0: # 不能for loop次数，因为需要判断能整除
            combination.append(factors[index])
            remain //= factors[index]
            self.dfs(index + 1, remain, factors, combination, results)
        for _ in range(len(combination) - size):
            combination.pop()    # 最后统一pop，因为combination每次加的是一个factor，而不是本factor的数量(硬币组合问题)，所以后面需要前面的结果