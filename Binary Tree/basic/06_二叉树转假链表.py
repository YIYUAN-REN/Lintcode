# Flatten Binary Tree to Linked List

"""
递归
base case: 若root为空，return
recursive: 
1. 找到left_last和right_last
2. root.left连空，root.right连root.left，left_last.right连root.right，返回当前树最后1个节点
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        if not root:
            return
        
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)

        if left_last:
            left_last.right = root.right
            root.right = root.left
            root.left = None
        
        return right_last or left_last or root
