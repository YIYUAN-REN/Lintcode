# Binary Tree Path Sum II

"""
思路：条件从 到达叶子节点 变成 path prefix
    不能用 if (prefix_sum - target) in visited 当作判断加results的条件，因为一条path可能有多个results，必须for loop扫一遍
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
    def binaryTreePathSum2(self, root, target):
        # write your code here
        results = []
        self.dfs(root, target, [], 0, results)
        return results
    
    def dfs(self, root, target, path, level, results):
        if not root:
            return
        
        path.append(root.val)

        # 检查当前path是否存在path_sum == target (包含当前节点)
        path_sum = 0
        for i in range(level, -1, -1):
            path_sum += path[i]
            if path_sum == target:
                results.append(path[i:])
        
        self.dfs(root.left, target, path, level + 1, results)
        self.dfs(root.right, target, path, level + 1, results)

        path.pop()