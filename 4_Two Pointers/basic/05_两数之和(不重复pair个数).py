# Two Sum - Unique pairs

"""
双指针方法1：时间O(nlogn) 空间O(1)
思路：相同元素的略过
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        
        while left < right:
            if nums[left] + nums[right] == target:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:    # left < right防止数组越界
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        
        return count


"""
双指针方法2：时间O(nlogn) 空间O(1)
思路：记录上次pair，若不同则记录
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        nums.sort()
        left, right = 0, len(nums) - 1
        last_pair = (None, None)
        count = 0

        while left < right:
            if nums[left] + nums[right] == target:
                if (nums[left], nums[right]) != last_pair:
                    count += 1
                last_pair = (nums[left], nums[right])
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

        return count


"""
hashmap方法：时间O(n) 空间O(n)
思路：count增加条件---循环hashmap元素时，num==(target-num)且hashmap计数>1 或 num<(target-num)且hashmap存在(target-num)
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                visited[nums[i]] += 1
            else:
                visited[nums[i]] = 1
        
        count = 0
        for num in visited.keys():
            diff = target - num
            if num == diff and visited[diff] > 1 or \
                num < diff and diff in visited: # num < diff保证(num, diff)组合只被计数1次，num在hashmap中只出现1次
                count += 1
        
        return count