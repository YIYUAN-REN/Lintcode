# Word Pattern

"""
思路：hashmap，会返回false的情况（pattern和str长度不同，pattern和str没一一对应）
1. 若(单词数)长度不同，返回false
2. 若(单词数)长度相同
    逐个匹配 pattern每个字母 和 str每个单词
    2.1 若pattern字母在map里
        若map里字母对应的单词 跟 str单词 不同，return false
    2.2 若pattern字母不在map里
        若str单词不在map里，return false
        否则，加入map
"""

class Solution:
    """
    @param pattern: a string, denote pattern string
    @param teststr: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, str):
        # write your code here
        words = str.split(' ')
        if len(pattern) != len(words):        # 1
            return False
        
        mapping = {}                        # 2
        for i in range(len(pattern)):
            letter, word = pattern[i], words[i]
            if letter in mapping:               # 2.1
                if mapping[letter] != word:
                    return False
            else:                               # 2.2
                if word in mapping.values():
                    return False
                mapping[letter] = word
        
        return True