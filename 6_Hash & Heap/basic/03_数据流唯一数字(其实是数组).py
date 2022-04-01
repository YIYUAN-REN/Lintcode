# First Unique Number in Data Stream

"""
思路: hashmap + doubly linked list (为了remove方法)

注：hashmap表示key-node，若key-None则表示该key非第一次遍历到
"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def __init__(self):
        self.key_to_node = {}
        self.dummy_head, self.dummy_tail = LinkedNode(0), LinkedNode(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head


    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def firstUniqueNumber(self, nums, number):  # 相当于get方法, 求到达number前nums出现的第一个唯一数字
        # Write your code here
        found = False
        for num in nums:
            # 若不是数组而是数据流，则下面为单独的add方法
            if num not in self.key_to_node:
                self.add_end(num)
            elif self.key_to_node[num]:   # 非唯一的情况
                self.remove(num)
            
            if num == number:
                found = True
                break
        
        return self.dummy_head.next.val if found else -1
    

    def add_end(self, key):
        node = LinkedNode(key)
        prev, next = self.dummy_tail.prev, self.dummy_tail

        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        
        self.key_to_node[key] = node


    def remove(self, key):
        node = self.key_to_node[key]
        next, prev = node.next, node.prev
        
        prev.next = next
        next.prev = prev
        
        self.key_to_node[key] = None
