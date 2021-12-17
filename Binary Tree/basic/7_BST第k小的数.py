# Kth Smallest Element in a BST

"""
思路：中序遍历，返回第k个元素
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        inorder = []
        self.traversal(root, inorder, k)
        return inorder[k - 1]
    
    
    def traversal(self, root, inorder, k):
        if not root:
            return
        
        self.traversal(root.left, inorder, k)
        inorder.append(root.val)
        self.traversal(root.right, inorder, k)