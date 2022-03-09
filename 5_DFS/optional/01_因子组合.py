# Factor Combinations

"""
Ӳ����ϱ��֣��Ѽӷ��ĳɳ˷�
1. �ҵ�����factors
2. ��factors��Ϊ"Ӳ�ұ�ֵ"������dfs(�ӷ���˷�)
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
        
        # ��0��factor�����
        self.dfs(index + 1, remain, factors, combination, results)

        # ��1��n��factor�����
        size = len(combination)
        while remain % factors[index] == 0: # ����for loop��������Ϊ��Ҫ�ж�������
            combination.append(factors[index])
            remain //= factors[index]
            self.dfs(index + 1, remain, factors, combination, results)
        for _ in range(len(combination) - size):
            combination.pop()    # ���ͳһpop����Ϊcombinationÿ�μӵ���һ��factor�������Ǳ�factor������(Ӳ���������)�����Ժ�����Ҫǰ��Ľ��