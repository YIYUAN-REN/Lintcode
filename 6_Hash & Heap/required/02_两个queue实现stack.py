# Implement Stack by Two Queues

"""
|___________|     |__________|
  q2：helper        q1：入栈

push: 加入q1
pop: q1元素移到q2(保留1个并删除)，若q1为空，交换q1和q2
top: q1元素移到q2(保留1个并不删除)，若q1为空，交换q1和q2
"""

class Stack:
    
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
        
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queue1.append(x)
        
    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        element = self.shuffle()
        return element

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        element = self.shuffle()
        self.queue1.append(element)
        return element

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not self.queue1 and not self.queue2
    
    
    def shuffle(self):
        # 将queue1前n-1个放入queue2，获得最后的元素
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        element = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return element