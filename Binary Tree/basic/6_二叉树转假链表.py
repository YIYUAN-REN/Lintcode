# Flatten Binary Tree to Linked List

"""
递归
base case: 若root为空，return
recursive: root.left连空，root.right连左子树头，左子树尾.right连root.right
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
            return None
        
        left = self.flatten(root.left)
        right = self.flatten(root.right)
        
        if left:
            # 连接left_last和root.right
            left_last = left
            while left_last.right:
                left_last = left_last.right
            left_last.right = root.right
            
            root.left = None
            root.right = left
        
        return root