# Kth Smallest Element in a BST

# 递归方法1: 空间O(1)
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
    def __init__(self):
        self.count = 0
        self.result = None

    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.inorder(root, k)
        return self.result
    
    def inorder(self, root, k):
        if not root:
            return
                
        # 左
        self.inorder(root.left, k)
        # 中
        self.count += 1
        if self.count == k:
           self.result = root.val
        # 右
        self.inorder(root.right, k)


# 递归方法2: 空间O(k)

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


# 非递归方法 - BST迭代器
"""
思路：stack表示当前节点一路向西的结果，模拟系统运行
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
        dummy = TreeNode(0) # 若不用dummy，就需要初始化stack时加入root一路向西的结果
        dummy.right = root
        stack = [dummy]
        for _ in range(k):
            node = stack.pop()
            if node.right:     # 如果node.right存在，则从node.right一路向西加入stack
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return stack[-1].val