# Two Sum III - Data structure design

"""
思路：用hashmap，因为使用双指针需要排序数组，每次add都要维护成本太高
"""

class TwoSum:
    def __init__(self):
        self.numbers = {}
        
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number in self.numbers:
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for (number, count) in self.numbers.items():
            if value - number in self.numbers:
                if value - number != number or count > 1:
                    return True
        return False
                