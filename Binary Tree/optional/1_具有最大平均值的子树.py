# Subtree with Maximum Average

"""
递归
base case：若root为空，则返回0
recursive：根据left_sum & left_size和right_sum & right_size得到本层sum & size，更新global_max，返回包括sum & size
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
        self.max_avg = float('-inf')
        self.max_node = None
    
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.max_node
        
    def helper(self, root):
        if not root:
            return 0, 0
        
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        root_sum, root_size = root.val + left_sum + right_sum, 1 + left_size + right_size
        
        root_avg = root_sum / root_size
        if root_avg > self.max_avg:
            self.max_node = root
            self.max_avg = root_avg
        
        return root_sum, root_size
        