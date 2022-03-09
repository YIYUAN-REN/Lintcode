# Word Search II

"""
方法1: hashmap
"""
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        word_set = set(words)   # 转set为了快速判断word是否存在
        prefix_set = set()  # 若不建立prefix set, 则对board每个位置 遍历 每个单词的每个字母总共4层循环

        # 建立prefix set
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        # 从board每个位置都dfs
        results = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, board[i][j], set([(i, j)]), results, board, word_set, prefix_set)
        
        return list(results)
    

    def dfs(self, x, y, word, visited, results, board, word_set, prefix_set):
        if word not in prefix_set:
            return
        if word in word_set:
            results.add(word)
        
        for dx, dy in ([(0,-1), (0, 1), (-1, 0), (1, 0)]):
            next_x, next_y = x + dx, y + dy
            if self.is_valid(next_x, next_y, board, visited):
                visited.add((next_x, next_y))
                self.dfs(next_x, next_y, word + board[next_x][next_y], visited, results, board, word_set, prefix_set)
                visited.remove((next_x, next_y))
    

    def is_valid(self, x, y, board, visited):
        if not 0 <= x < len(board) or not 0 <= y < len(board[0]):
            return False
        if (x, y) in visited:
            return False
        return True
        


"""
方法2: Trie
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word
    
    def find(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return None
            node = node.children[c]
        return node


class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
         # 建立Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        # 从board每个位置都dfs
        results = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(i, j, set([(i, j)]), results, board, trie.root.children.get(board[i][j]))
        
        return list(results)
    

    def dfs(self, x, y, visited, results, board, node):
        if not node:
            return
        if node.is_word:
            results.add(node.word)
        
        for dx, dy in ([(0,-1), (0, 1), (-1, 0), (1, 0)]):
            next_x, next_y = x + dx, y + dy
            if self.is_valid(next_x, next_y, board, visited):
                visited.add((next_x, next_y))
                self.dfs(next_x, next_y, visited, results, board, node.children.get(board[next_x][next_y]))
                visited.remove((next_x, next_y))
    

    def is_valid(self, x, y, board, visited):
        if not 0 <= x < len(board) or not 0 <= y < len(board[0]):
            return False
        if (x, y) in visited:
            return False
        return True

