# Insert Delete GetRandom O(1) - Duplicates allowed

"""
思路：array + hashmap(记录array下标)
不能只用hashmap，因为hashmap会去重，而getRandom根据元素重复个数概率不同
1. 插入：若不存在，插入到array最后，更新hashmap
2. 删除：若存在，将最后位复制到当前位与并删除最后位，更新hashmap
"""
import random

class RandomizedSet:
    
    def __init__(self):
        # do intialization if necessary
        self.array = []
        self.mapping = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.mapping:
            return False
        self.array.append(val)
        self.mapping[val] = len(self.array) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.mapping:
            return False
        index, last = self.mapping[val], self.array[-1]
        self.array[index] = last
        self.array.pop()
        self.mapping[last] = index
        del self.mapping[val]
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        index = random.randint(0, len(self.array) - 1)
        return self.array[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()