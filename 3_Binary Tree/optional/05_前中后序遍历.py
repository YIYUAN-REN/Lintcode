# Binary Tree Preorder/Inorder/Postorder Traversal

"""
方法1：递归
1. base case: 最下层空节点，直接终止
2. recursive rule: result添加当前node，再往左走，再往右走
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
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        results = []
        self.traversal(root, results)
        return results
    
    
    def traversal(self, root, results):
        if not root:
            return
        
        self.traversal(root.left, results)
        self.traversal(root.right, results)
        results.append(root.val)


"""
方法2：迭代(stack模拟系统)
preorder: 初始stack=[root], 每次pop后，栈先push右后push左(为了先pop左后pop右)
inorder: 初始stack=[一直到leftmost], 每次pop后，栈push右直到leftmost
postorder: preorder变体(中左右->中右左).reverse
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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        results = []
        stack = [root]
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return results
    
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        # 初始化stack
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        results = []
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return results
    
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(reversed(result))