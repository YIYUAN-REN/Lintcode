# k Sum II

"""
方法1：加/不加
每层代表的意义：层数 = n，每层决定加/不加
每层多少个状态：状态数 = 2

Time O(2^n)
"""

class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(nums)
    @param target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, nums, k, target):
        # write your code here
        results = []
        self.dfs(0, nums, k, target, [], results)
        return results
    
    def dfs(self, index, nums, k, remain, combination, results):
        if len(combination) == k and remain == 0:   # 得到结果
            results.append(list(combination))
            return
        if index == len(nums) or len(combination) >= k or remain <= 0:  # 剪枝
            return
        
        combination.append(nums[index])
        self.dfs(index + 1, nums, k, remain - nums[index], combination, results)
        combination.pop()
        self.dfs(index + 1, nums, k, remain, combination, results)



"""
方法2：加哪个
每层代表的意义：层数 = k，每层决定加哪个数(到第k层中止)
每层多少个状态：状态数 = 未被使用numbers数量

Time O(k ^ 剩余numbers数量)
"""

class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(nums)
    @param target: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, nums, k, target):
        # write your code here
        results = []
        self.dfs(0, sorted(list(nums)), k, target, [], results)
        return results
    
    
    def dfs(self, index, nums, k, remain, combination, results):
        if k == 0 and remain == 0:
            results.append(list(combination))
            return
        if k == 0 or remain <= 0:
            return
        
        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(i + 1, nums, k - 1, remain - nums[i], combination, results)
            combination.pop()