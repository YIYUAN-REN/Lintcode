# Lowest Common Ancestor of a Binary Tree

"""
递归
base case: 若root为A或B，返回root；若root为空，返回空
recursive: 找左右子树的lca。若都存在返回root；若存在左或右，返回左或右；若不存在返回空
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        result = self.lca(root, A, B)
        if not result:
            return None
        if result == A:
            return A if self.lca(root, B, B) else None
        if result == B:
            return B if self.lca(root, A, A) else None
        return result
    
    
    def lca(self, root, A, B):
        if not root:
            return None
        if root == A or root == B:
            return root
        
        left = self.lca(root.left, A, B)
        right = self.lca(root.right, A, B)
        
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        return None
