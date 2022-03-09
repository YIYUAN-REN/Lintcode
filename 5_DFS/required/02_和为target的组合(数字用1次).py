# Combination Sum II

"""
方法1
每层代表的意义：n层，每层决定放/不放
每层多少个状态：2个状态，放/不放
"""

class Solution:
    """
    @param nums: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, nums, target):
        # write your code here
        results = []
        nums.sort()
        self.dfs(0, [], nums, target, results)
        return results
    
    
    def dfs(self, index, combination, nums, remain, results):
        if remain == 0:
            if combination not in results:
                results.append(list(combination))
            return
        if remain < 0 or index == len(nums):
            return
        
        combination.append(nums[index])
        self.dfs(index + 1, combination, nums, remain - nums[index], results)
        combination.pop()
        self.dfs(index + 1, combination, nums, remain, results)


"""
方法2
每层代表的意义：n层，每层决定放哪个
每层多少个状态：?个状态，放哪个
"""

class Solution:
    """
    @param nums: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, nums, target):
        # write your code here
        results = []
        self.dfs(0, [], sorted(nums), target, results)  # nums排序，因为之后要跳过相同元素
        return results
    
    
    def dfs(self, index, combination, nums, remain, results):
        if remain < 0:      # index == len(nums)进不了循环
            return
        if remain == 0:
            results.append(list(combination))
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:	# 每层防止出现重复，比如出现过本层放1就没必要再放1了
                continue
            combination.append(nums[i])
            self.dfs(i + 1, combination, nums, remain - nums[i], results)   # i+1而不是index+1，否则会有重复组合
            combination.pop()
