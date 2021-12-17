# Lowest Common Ancestor II

"""
思路
1. A一直走到root，中间记录所有nodes
2. B一直走到root，若出现在node中，则返回
"""
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        visited = set()
        while A:
            visited.add(A)
            A = A.parent
        
        while B:
            if B in visited:
                return B
            B = B.parent
        
        return None