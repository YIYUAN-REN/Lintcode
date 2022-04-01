# Implement Queue by Two Stacks

"""
_____| s2   s1 |_____
pop: 若s2为空，移到s2再pop
"""

class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []
        
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)
        
    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.shuffle()
        return self.stack2.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        self.shuffle()
        return self.stack2[-1]
    
    
    def shuffle(self):
        if self.stack2:
            return
        while self.stack1:
            self.stack2.append(self.stack1.pop())