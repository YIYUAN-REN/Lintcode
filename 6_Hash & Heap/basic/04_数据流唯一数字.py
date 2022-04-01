# First Unique Number in Data Stream II

"""
思路: hashmap + doubly linked list (为了remove方法)

注：hashmap表示key-node，若key-None则表示该key非第一次遍历到
"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        

class DataStream:
    def __init__(self):
        # do intialization if necessary
        self.key_to_node = {}
        self.dummy_head, self.dummy_tail = LinkedNode(0), LinkedNode(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
          
    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num not in self.key_to_node:
            self.add_end(num)
        elif self.key_to_node[num]:   # 非唯一的情况
            self.remove(num)


    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        return self.dummy_head.next.val
    

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
        