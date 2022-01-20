# Inorder Predecessor in BST

"""
思路：BST遍历就是中序遍历。一路向下，找最大小于目标的节点
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
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        predecessor = None
        while root:
            if root.val >= p.val:
                root = root.left
            else:
                predecessor = root
                root = root.right
        return predecessor