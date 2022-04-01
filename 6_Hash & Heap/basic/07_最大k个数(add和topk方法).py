# Top k Largest Numbers II

"""
思路: add()时维护min_heap大小不超过k, 保证topk()不用额外heappop计算
"""

import heapq

class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        # do intialization if necessary
        self.min_heap = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        # write your code here
        heapq.heappush(self.min_heap, num)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    """
    @return: Top k element
    """
    def topk(self):
        # write your code here
        return self.min_heap
