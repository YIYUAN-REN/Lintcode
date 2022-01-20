# Validate Binary Search Tree

"""
递归
1. base case：node为空时，返回True
2. recursive rule：
    若node在(min, max)区间，继续向左向右
    否则，返回False
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        return self.helper(root, float('-inf'), float('inf'))
    
    
    def helper(self, root, min, max):
        if not root:
            return True
        
        if min < root.val < max:
            left = self.helper(root.left, min, root.val)
            right = self.helper(root.right, root.val, max)
            return left and right
        return False