# LRU Cache

"""
������ݽṹ
set��Ҫ����: �鿴�Ƿ����+ɾ����ǰ+ͷ����ӵ�ǰ+ɾ��β��
get��Ҫ���ܣ��鿴�Ƿ����+ɾ����ǰ+ͷ����ӵ�ǰ
1. �ҵ��Ƿ���ڣ�hash
2. ���/ɾ��Ԫ�أ�˫������

ע��hash��ʾkey-node����key-val
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
        
    def remove(self, key):  # ͬʱɾ��hashmap������
        node = self.key_to_node[key]
        next, prev = node.next, node.prev
        
        prev.next = next
        next.prev = prev
        
        del self.key_to_node[key]
    
    def add_head(self, key, value):  # ͬʱ���hashmap������
        node = LinkedNode(key, value)
        head = self.dummy_head.next
        
        head.prev = node
        node.next = head
        self.dummy_head.next = node
        node.prev = self.dummy_head
        
        self.key_to_node[key] = node
    