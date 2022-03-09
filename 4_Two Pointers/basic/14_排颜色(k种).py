"""
思路：彩虹排序(基本等于快速排序。增加color_from和color_to，把pivot换成mid_color)
    表现更好因为不是根据pivot_pos而是pivot/mid的值来划分左右

    快速排序: 时间O(nlogn)--因为栈logn层(以元素为单位划分) 空间O(1)
    计数排序: 时间O(n) 空间O(k)
    彩虹排序: 时间O(nlogk)--因为栈logk层(以颜色为单位划分) 空间O(1)
"""

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.rainbow_sort(0, len(colors) - 1, 0, k, colors)
    

    def rainbow_sort(self, start, end, color_start, color_end, nums):
        if start >= end or color_start == color_end:
            return
        
        pivot_pos, color = self.partition(start, end, nums)
        self.rainbow_sort(start, pivot_pos - 1, color_start, color - 1, nums)   # color-1 因为pivot_pos左侧没有color的值
        self.rainbow_sort(pivot_pos + 1, end, color, color_end, nums)   # color 因为pivot_pos右侧有color的值
    

    def partition(self, start, end, nums):
        pivot_pos = start + (end - start) // 2
        pivot = nums[pivot_pos]
        nums[pivot_pos], nums[end] = nums[end], nums[pivot_pos]
        
        left, right = start, end - 1
        while left <= right:
            if nums[left] < pivot:
                left += 1
            elif nums[right] >= pivot:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        nums[right + 1], nums[end] = nums[end], nums[right + 1] # 必须换回来, 因为pivot要参与下次sort
        
        return right + 1, pivot