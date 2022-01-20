# Closest Binary Search Tree Value

"""
方法1
思路：不断收拢上下边界
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
        lower, upper = float('-inf'), float('inf')
        while root:
            if root.val < target:
                lower = root.val
                root = root.right
            elif root.val > target:
                upper = root.val
                root = root.left
            else:
                return root.val
        
        if abs(lower - target) <= abs(upper - target):
            return lower
        return upper


# 方法2
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