# Closest Binary Search Tree Value II

"""
思路：按照找最接近1个值的思路将路径加入stack，根据prev_stack和next_stack的栈顶哪个更接近来决定prev()或者next()，直到找到k个
Time: O(k + h)
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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here

        # 不能初始化为root一路向西,因为这里找的是第k接近而不是第k小
        prev_stack = self.get_stack(root, target)  # 只进行prev()
        next_stack = list(prev_stack) # 只进行next()

        # 避免两个stack出现重复的初始结果
        if prev_stack[-1].val < target:
            self.next(next_stack)
        else:
            self.prev(prev_stack)
        
        # 找k个结果
        results = []
        for _ in range(k):
            if self.is_closer(prev_stack, next_stack, target):
                results.append(prev_stack[-1].val)
                self.prev(prev_stack)
            else:
                results.append(next_stack[-1].val)
                self.next(next_stack)
        
        return results
    
    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return stack
    
    def next(self, stack):
        if stack[-1].right:
            node = stack[-1].right  # 不能pop删除，因为stack路径不是一路向西
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:    # 一路从东pop删除
                node = stack.pop()

    def prev(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
    
    def is_closer(self, stack1, stack2, target):
        if not stack1:
            return False
        if not stack2:
            return True
        return abs(stack1[-1].val - target) < abs(stack2[-1].val - target)
