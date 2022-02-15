# 3Sum Closest

"""
思路：for loop + 趋近target过程中随时更新min diff
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        min_diff = float('inf')
        result = -1
        
        for i in range(2, len(nums)):
            # two sum
            left, right = 0, i - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if abs(sum - target) < min_diff:
                    result = sum
                    min_diff = min(min_diff, abs(sum - target))
                    
                if sum == target:
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
        
        return result   # 返回三元组和