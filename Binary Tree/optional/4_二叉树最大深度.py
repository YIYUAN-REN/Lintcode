# Maximum Depth of Binary Tree

"""
方法1：
递归
               root
            /       \       ↑
        N1              N2
      /     \         /     \       ↑
    N11     N12    N21      N22

1. base case: 最下层空节点，返回0
2. recursive rule: 当前高度 = max(左子树高度, 右子树高度) + 1

方法2：分层BFS
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
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        
        queue = collections.deque([root])
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return level