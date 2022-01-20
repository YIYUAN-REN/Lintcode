# Binary Tree Path Sum

"""
递归DFS
base case：若root为空，终止；若root左右为空，更新results
recursive：往左往右，增加path prefix
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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        results = []
        self.dfs(root, target, [], 0, results)
        return results
    
    
    def dfs(self, root, target, path, path_sum, results):
        if not root:
            return
        
        # 检查叶子节点需包括节点本身
        if not root.left and not root.right:
            if path_sum + root.val == target:
                path.append(root.val)
                results.append(list(path))
                path.pop()
            return
        
        path.append(root.val)   
        self.dfs(root.left, target, path, path_sum + root.val, results)
        self.dfs(root.right, target, path, path_sum + root.val, results)
        path.pop()  # 只有回到本层才pop