# String Permutation II / Permutations II

"""
思路：DFS（避免同层加入相同元素）
"""

"""
方法1：经典
每层代表的意义：层数 = string长度，每层决定加哪个char
每层多少个状态：状态数 = 未被使用chars数量

base case：若permutation长度 = string长度，放入results
recursive rule：
  case 1 ... case n：放入未被使用char
"""

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        str = sorted(list(str)) # str要排序，因为permutation时根据前一个元素判断是否是重复元素
        visited = [False] * len(str)    # visited不能是set()，因为重复元素要判断index是否访问过
        results = []
        self.dfs(str, visited, [], results)
        return results
        
    
    def dfs(self, str, visited, permutation, results):
        if len(permutation) == len(str):
            results.append(''.join(permutation))
            return
        
        for i in range(len(str)):
            if visited[i]:
                continue
            if i > 0 and str[i] == str[i-1] and not visited[i-1]:
                continue
            
            permutation.append(str[i])
            visited[i] = True
            self.dfs(str, visited, permutation, results)
            visited[i] = False
            permutation.pop()


"""
方法2：swap-swap
每层代表的意义：层数 = string长度，每层决定index位置是哪个char
每层多少个状态：状态数 = index位置(包含index)后chars数量

base case：若index = string长度，放入results
recursive rule：
  case 1 ... case n：把 index位置(包含index)后的char 交换到index位置
"""

class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        results = []
        self.dfs(0, list(str), results)
        return results
    
    
    def dfs(self, index, str, results):
        if index == len(str):
            results.append(''.join(str))
            return
        
        visited = set() # 局部visited用于排除该轮swap的重复元素
        for i in range(index, len(str)):
            if str[i] in visited:
                continue
                
            visited.add(str[i])
            str[index], str[i] = str[i], str[index]
            self.dfs(index + 1, str, results)
            str[index], str[i] = str[i], str[index]