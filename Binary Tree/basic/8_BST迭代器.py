# Binary Search Tree Iterator

"""
思路：stack表示当前节点一路向西的结果，模拟系统运行。next()时顺便添加stack
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        dummy = TreeNode(0) # 若不用dummy，就需要在__init__手动初始化stack
        dummy.right = root
        self.stack = [dummy]
        self.next() # 初始化stack时加入root一路向西的结果

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self, ):
        # write your code here
        result = self.stack.pop()
        node = result.right
        while node:
            self.stack.append(node)
            node = node.left
        return result

