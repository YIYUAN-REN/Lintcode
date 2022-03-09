# Word Pattern II

"""
思路：基于word pattern，pattern逐个匹配，string每种都试试

每层代表的意义：n层，每层决定单词是什么
每层多少个状态：?个状态，单词给几个字母
"""

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, string):
        return self.dfs(pattern, string, {})
    
    # dfs表示match与否
    def dfs(self, pattern, string, mapping):
        # 1. 若(单词数)长度相同, 即都走完了
        if len(pattern) == 0 and len(string) == 0:
            return True
        
        # 2. 若(单词数)长度不同
        
        # 2.1 若pattern字母在map里
        letter = pattern[0]
        if letter in mapping:
            word = mapping[letter]
            # 若map里pattern字母对应的 != 单词, 则false
            if not string.startswith(word):
                return False
            # 若之后存在完全匹配, 则true
            if self.dfs(pattern[1:], string[len(word):], mapping):
                return True
        
        # 2.2 若pattern字母不在map里，枚举string每种可能的单词
        for i in range(len(string)):
            word = string[:i + 1]
            # 若单词在map里, 则跳过
            if word in mapping.values():
                continue
            # 若之后存在完全匹配, 则true
            mapping[letter] = word
            if self.dfs(pattern[1:], string[i + 1:], mapping):
                return True
            del mapping[letter]
        
        return False
        