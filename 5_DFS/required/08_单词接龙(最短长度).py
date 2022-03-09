# Word Ladder

"""
思路：分层BFS（每层generate所有可能的下个word）
        hit
    kit hat hiv
 ... ... ... ... ...
"""

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])
        level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return level
                
                for next_word in self.get_next_words(word, visited, dict):
                    queue.append(next_word)
                    visited.add(next_word)
        
        return -1
    
    
    def get_next_words(self, word, visited, dict):
        results = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word in dict and next_word not in visited:
                    results.append(next_word)
        return results