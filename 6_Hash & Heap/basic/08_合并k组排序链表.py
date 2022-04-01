# Merge K Sorted Lists

"""
思路：每个链表起始节点放入heap，pop哪个链表就加对应链表的下个节点
"""

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

import heapq

ListNode.__lt__ = lambda x, y: (x.val < y.val)

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        dummy = cur = ListNode(0)
        min_heap = []
        
        for node in lists:
            if node:
                heapq.heappush(min_heap, node)
        
        while min_heap:
            node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, node.next)
                
            cur.next = node
            cur = cur.next
        
        return dummy.next