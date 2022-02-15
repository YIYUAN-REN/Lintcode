# Remove Duplicate Numbers in Array

"""
思路1：不排序，hashset + 快慢指针
Time O(n), Space O(n)
"""

class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        dedup = set()
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] not in dedup:
                dedup.add(nums[fast])
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow   # 返回元素个数
        
"""
思路2：排序，快慢指针
Time O(nlogn), Space O(1)
"""
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        slow = fast = 1
        while fast < len(nums):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow   # 返回元素个数
