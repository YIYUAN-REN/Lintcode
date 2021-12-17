# Minimum Subtree

"""
递归
base case: 若root为空，返回极大值
recursive: 找到左子和与右子和，更新global_min，返回左子和+右子和+自己
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    
    def __init__(self):
        self.min_sum = float('inf')
        self.min_root = None
    
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        root_sum = self.helper(root)
        if root_sum < self.min_sum:
            self.min_root = root
        
        return self.min_root
    
    
    def helper(self, root):
        if not root:
            return 0
        
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        
        if root.left and left_sum < self.min_sum:
            self.min_sum = left_sum
            self.min_root = root.left
        if root.right and right_sum < self.min_sum:
            self.min_sum = right_sum
            self.min_root = root.right
        
        return left_sum + root.val + right_sum