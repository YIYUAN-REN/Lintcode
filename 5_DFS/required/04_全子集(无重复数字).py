# Subsets

"""
方法1
每层代表的意义：n层，每层决定是否放入element
每层多少个状态：2个状态，放入和不放入
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        results = []
        self.dfs(0, [], nums, results)
        return results
    
    
    def dfs(self, index, combination, nums, results):
        if index == len(nums):
            results.append(list(combination))
            return
        
        combination.append(nums[index])
        self.dfs(index + 1, combination, nums, results)
        combination.pop()
        self.dfs(index + 1, combination, nums, results)



"""
方法2
每层代表的意义：n层，每层决定放入哪个element
每层多少个状态：?个状态
"""

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        results = []
        self.dfs(0, [], nums, results)
        return results
    

    def dfs(self, index, combination, nums, results):
        results.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(i + 1, combination, nums, results)
            combination.pop()