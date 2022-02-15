# Lowest Common Ancestor III

"""
递归
base case：若root为空，则返回空；若root为p或q，则返回p或q
recursive：若左右子树都有p、q，则返回root；若只有左子树有，则返回left；若只有右子树有，则返回right；若都没有，则返回空
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