# Middle of the Linked List (相对靠左)

"""
思路：快慢指针
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """
    def middleNode(self, head):
        # write your code here
        if not head:
            return None
        
        slow = fast = head
        while fast.next and fast.next.next:	# 若返回相对靠右中点，则while fast and fast.next
            slow = slow.next
            fast = fast.next.next
        return slow