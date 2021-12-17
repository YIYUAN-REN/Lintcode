# Closest Binary Search Tree Value

"""
思路：一路到底，不断更新global
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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        min_diff, result = abs(root.val - target), root.val
        
        while root:
            if root.val < target:
                if abs(root.val - target) < min_diff:
                    result = root.val
                    min_diff = abs(root.val - target)
                root = root.right
                
            elif root.val > target:
                if abs(root.val - target) < min_diff:
                    result = root.val
                    min_diff = abs(root.val - target)
                root = root.left
                
            else:
                return root.val
        
        return result