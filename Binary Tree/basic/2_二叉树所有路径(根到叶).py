# Binary Tree Paths

"""
思路：DFS（path走到叶子节点为止）
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        
        results = []
        self.dfs(root, results, [str(root.val)]) #root为每个path的头
        return results
    
    
    def dfs(self, root, results, path):
        if not root.left and not root.right:
            results.append('->'.join(path))
            return
        
        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, results, path)
            path.pop()

        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, results, path)
            path.pop()