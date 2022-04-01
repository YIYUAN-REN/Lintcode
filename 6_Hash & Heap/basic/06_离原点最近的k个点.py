# K Closest Points

"""
方法1: max_heap维持大小不超过k，来保证单次push的复杂度不超过O(logk)，再pop k次找到结果

Time: O(nlogk)
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        max_heap = []
        for point in points:
            dist = (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
            heapq.heappush(max_heap, (-dist, -point.x, -point.y))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        results = []
        for _ in range(k):
            _, x, y = heapq.heappop(max_heap)
            results.append([-x, -y])

        return results



"""
方法2: min_heap pop k次找到结果

Time: O(nlogn)
"""

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

import heapq

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        min_heap = []
        for point in points:
            dist = (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
            heapq.heappush(min_heap, (dist, point.x, point.y))
        
        results = []
        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            results.append([x, y])
        
        return results



"""
方法3: 快速选择

Time: O(n + klogk)
"""