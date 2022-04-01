# LRU Cache

"""
设计数据结构
set需要功能: 查看是否存在+删除当前+头部添加当前+删除尾部
get需要功能：查看是否存在+删除当前+头部添加当前
1. 找到是否存在：hash
2. 添加/删除元素：双向链表

注：hash表示key-node而非key-val
"""

class LinkedNode:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.dummy_head, self.dummy_tail = LinkedNode(0, 0), LinkedNode(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        
        self.capacity = capacity
        self.key_to_node = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_node:
            return -1
        
        value = self.key_to_node[key].val
        self.remove(key)
        self.add_head(key, value)
        
        return value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_node:
            self.remove(key)
        
        self.add_head(key, value)
        
        if len(self.key_to_node) > self.capacity:
            self.remove(self.dummy_tail.prev.key)
        
    def remove(self, key):  # 同时删除hashmap和链表
        node = self.key_to_node[key]
        next, prev = node.next, node.prev
        
        prev.next = next
        next.prev = prev
        
        del self.key_to_node[key]
    
    def add_head(self, key, value):  # 同时添加hashmap和链表
        node = LinkedNode(key, value)
        head = self.dummy_head.next
        
        head.prev = node
        node.next = head
        self.dummy_head.next = node
        node.prev = self.dummy_head
        
        self.key_to_node[key] = node
    