# Letter Combinations of a Phone Number II

"""
方法1: hashmap统计每个query的数字匹配单词的个数
"""

"""
方法2: Trie存每个dict的单词转化成数字的字符串
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.num_words = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.num_words += 1
    
    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node
    

REVERSE_KEYBOARD = {
    "a": "2", "b": "2", "c": "2", 
    "d": "3", "e": "3", "f": "3", 
    "g": "4", "h": "4", "i": "4", 
    "j": "5", "k": "5", "l": "5", 
    "m": "6", "n": "6", "o": "6", 
    "p": "7", "q": "7", "r": "7", 
    "s": "7", "t": "8", "u": "8", 
    "v": "8", "w": "9", "x": "9", 
    "y": "9", "z": "9",
}

class Solution:
    """
    @param queries: the queries
    @param dict: the words
    @return: return the queries' answer
    """
    def letterCombinationsII(self, queries, dict):
        # word -> digits, insert to Trie
        trie = Trie()
        for word in dict:
            trie.insert(''.join(REVERSE_KEYBOARD[c] for c in word))

        # find and get counts
        results = []
        for digits in queries:
            node = trie.find(digits)
            results.append(node.num_words if node else 0)
        
        return results