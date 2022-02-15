# Minimum Depth of Binary Tree

"""
思路：分层BFS
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
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        
        queue = collections.deque([root])
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:    # 到达最近叶子节点
                    return level
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    