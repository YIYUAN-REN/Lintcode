# 3Sum

"""
思路：for loop + two sum
"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        
        results = []
        for i in range(len(numbers) - 2):
            # 去重c
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            self.two_sum(numbers, i, results)
            
        return results
    
    
    def two_sum(self, nums, i, results):
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + nums[i] == 0:
                results.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # 去重a和b
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif nums[left] + nums[right] + nums[i] < 0:
                left += 1
            
            else:
                right -= 1