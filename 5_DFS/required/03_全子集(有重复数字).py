# Subsets II

"""
方法1
正常subsets，但(加/不加)在进行 不加的dfs 前需跳过所有相同元素

类比Combination Sum II（加哪个）：每层会有重复元素，跳过所有重复
Subsets II（加/不加）：不加当前元素时，跳过后续重复元素
"""

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        results = []
        self.dfs(0, [], sorted(nums), results)  # nums排序，因为之后要跳过相同元素
        return results
    
    
    def dfs(self, index, combination, nums, results):
        if index == len(nums):
            results.append(list(combination))
            return
        
        combination.append(nums[index])
        self.dfs(index + 1, combination, nums, results)
        combination.pop()
        
        while index < len(nums) - 1 and nums[index + 1] == nums[index]: # 不能判断nums[index] == nums[index-1]，因为在"不加"分支会把当前index加进来，下一层"加"分支index+1位置的重复元素仍存在
            index += 1
        
        self.dfs(index + 1, combination, nums, results)
            


"""
方法2
正常subsets，每层决定加哪个
"""

class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        results = []
        self.dfs(0, [], sorted(nums), results)  # nums排序，因为之后要跳过相同元素
        return results
    
    
    def dfs(self, index, combination, nums, results):
        results.append(list(combination))

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:	# 每层防止出现重复，比如出现过本层放1就没必要再放1了
                continue
            combination.append(nums[i])
            self.dfs(i + 1, combination, nums, results)
            combination.pop()