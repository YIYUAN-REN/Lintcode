# Triangle Count

"""
思路：3sum，每轮第三边为target，其余两边在小于第三边的范围找2sum (允许相同pair)
"""

class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, nums):
        # write your code here
        if len(nums) < 3:
            return 0
            
        nums.sort()
        count = 0
        
        for i in range(2, len(nums)):
            # two sum
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += (right - left) # 因为这里不是=，需要一次性把满足的结果加入再移动left
                    right -= 1
                else:
                    left += 1
        
        return count
        