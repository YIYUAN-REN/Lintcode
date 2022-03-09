# Permutations

"""
方法1：经典，每层决定放哪个
"""

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results = []
        self.dfs([], nums, set(), results)
        return results
    
    
    def dfs(self, permutation, nums, visited, results):
        if len(permutation) == len(nums):
            results.append(list(permutation))
            return
        
        for num in nums:
            if num in visited:
                continue
            permutation.append(num)
            visited.add(num)
            self.dfs(permutation, nums, visited, results)
            visited.remove(num)
            permutation.pop()


"""
方法2：swap-swap（更好，处理重复元素更方便），每层把每个都swap试试
"""

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results = []
        self.dfs(0, nums, results)
        return results
    
    
    def dfs(self, index, nums, results):
        if index == len(nums):
            results.append(list(nums))
            return
        
        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.dfs(index + 1, nums, results)
            nums[index], nums[i] = nums[i], nums[index]
