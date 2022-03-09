# Combination Sum

"""
方法1：每层决定放哪个
Time O(n ^ target/min_number)  Space O(n ^ target/min_number)
"""

"""
方法2：每层决定放几个当前的数   better!
"""

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        results = []
        candidates.sort()
        self.dfs(0, [], target, candidates, results)
        return results
    
    
    def dfs(self, index, combination, remain, candidates, results):
        if index == len(candidates):
            if remain == 0: # 必须在index == len(candidates)下，否则最后一个数是结果的话搜索不到
                results.append(list(combination))
            return
        
        for i in range(remain // candidates[index] + 1):
            for _ in range(i):
                combination.append(candidates[index])
            self.dfs(index + 1, combination, remain - candidates[index] * i, candidates, results)
            for _ in range(i):
                combination.pop()