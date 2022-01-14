# Minimum Subtree

"""
递归
base case: 若root为空，返回0
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
        self.min_val = float('inf')
        self.min_node = None

    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.helper(root)
        return self.min_node
    
    def helper(self, root):
        if not root:    # 可以if not root为空return来判断，因为当前节点返回取决于自己
            return 0
        
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        root_sum = left_sum + right_sum + root.val

        if root_sum < self.min_val:
            self.min_val = root_sum
            self.min_node = root

        return root_sum
