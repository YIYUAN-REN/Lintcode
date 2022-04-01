# Implement Stack

"""
思路: 链表全操作O(1), head为栈顶
"""

class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    """
    @param: val: An integer
    @return: nothing
    """
    def push(self, val):
        # write your code here
        node = LinkedNode(val)
        node.next = self.head
        self.head = node

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.head = self.head.next

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.head.val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not self.head
