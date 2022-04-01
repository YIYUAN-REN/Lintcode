# Ugly Number II

"""
思路：每轮heap pop出的数分别乘2,3,5加入heap，重复n次

注意: 丑数包含1
"""

import heapq

class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        min_heap = [1]
        visited = set([1])  # 可能有重复，比如1*2*3 = 1*3*2
        
        for _ in range(n):
            num = heapq.heappop(min_heap)
            for factor in [2, 3, 5]:
                if num * factor in visited:
                    continue
                heapq.heappush(min_heap, num * factor)
                visited.add(num * factor)
        
        return num