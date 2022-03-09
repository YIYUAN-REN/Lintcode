# Find the Missing Number II

"""
思路：DFS搜索所有可能组合，找到唯一正确的组合，再找到缺失的数
"""

class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # 找到正确的数字组合
        result = []
        self.dfs(0, [], n, str, result)
        
        # 找到缺失的数
        for i in range(1, n + 1):
            if i not in result:
                return i
        return -1
    

    def dfs(self, index, combination, n, str, result):
        if result: # 剪枝
            return
        
        if index == len(str):
            if len(combination) == n - 1:
                result.extend(combination)
            return
        
        if len(combination) == n - 1: # 剪枝
            return
        
        # recursion
        for i in range(1, 3):   # given n < 100
            if index + i > len(str):    # 越界
                break
                
            num = int(str[index:index+i])
            if num in combination or num > n or str[index] == '0':
                continue

            combination.append(num)
            self.dfs(index + i, combination, n, str, result)
            combination.pop()
