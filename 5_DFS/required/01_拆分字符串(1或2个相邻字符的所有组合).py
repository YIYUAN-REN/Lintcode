# Split String

"""
每层代表的意义：n层，每层决定是否放1个/2个字符
每层多少个状态：2个状态，放1个和放2个
"""

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        results = []
        self.dfs(0, [], s, results)
        return results
    
    
    def dfs(self, index, combination, s, results):
        if index == len(s):
            results.append(list(combination))
            return
        
        for i in range(1, 3):
            if index + i <= len(s): # 必须有=，因为s[index: index + i]不包括index + i位置的字符
                combination.append(s[index: index + i])
                self.dfs(index + i, combination, s, results)
                combination.pop()