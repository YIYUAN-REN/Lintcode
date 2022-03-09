# Combinations

"""
方法1
思路：DFS放/不放，注意剪枝（剩余数字不够）
"""

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results = []
        self.dfs(1, [], n, k, results)
        return results
    
    
    def dfs(self, index, combination, n, k, results):
        if len(combination) == k:
            results.append(list(combination))
            return
        
        if index == n + 1:
            return
        
        # 剪枝：若后面数放入仍不够k
        if len(combination) + n - index + 1 < k:
            return
        
        combination.append(index)
        self.dfs(index + 1, combination, n, k, results)
        combination.pop()
        self.dfs(index + 1, combination, n, k, results)



"""
方法2
思路：DFS放哪个，注意剪枝（剩余数字不够）
"""

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        results = []
        self.dfs(1, [], n, k, results)
        return results
    
    def dfs(self, index, combination, n, k, results):
        if len(combination) == k:
            results.append(list(combination))
            return

        if index == n + 1 or len(combination) + n - index + 1 < k:
            return
        
        for i in range(index, n + 1):
            combination.append(i)
            self.dfs(i + 1, combination, n, k, results)
            combination.pop()
