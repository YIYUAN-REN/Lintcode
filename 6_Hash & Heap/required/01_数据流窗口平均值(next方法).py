# Moving Average from Data Stream

"""
思路：deque
"""

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.queue = collections.deque()
        self.sum = 0
        self.size = size

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        self.queue.append(val)
        self.sum += val
        
        if len(self.queue) > self.size:
            num = self.queue.popleft()
            self.sum -= num
        
        return self.sum / len(self.queue)
            

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)