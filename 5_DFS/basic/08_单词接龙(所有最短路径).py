# Word Ladder II

"""
方法1
思路：BFS找最短长度，DFS找到所有路径(满足最短长度)。超时！
"""

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        # write your code here
        results = []
        dict.add(end)
        
        distance = self.bfs(start, end, dict)
        if distance != -1:
            self.dfs(start, end, [start], dict, distance, results)
        return results
    
    def bfs(self, start, end, dict):
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
    
    def dfs(self, start, end, path, dict, distance, results):
        if len(path) == distance:
            if start == end:
                results.append(list(path))
            return
        
        for next_word in self.get_next_words(start, set(), dict):
            path.append(next_word)
            self.dfs(next_word, end, path, dict, distance, results)
            path.pop()
    
    def get_next_words(self, word, visited, dict):
        results = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word in dict and next_word not in visited:
                    results.append(next_word)
        return results
        


"""
方法2
思路：BFS建立map(从end到dict中每个单词的距离)，DFS找到所有路径(利用map剪枝)
"""

class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)
        distance = {}   # 每个单词与end的距离
        results = []
        
        self.bfs(end, distance, dict)
        self.dfs(start, end, distance, dict, [start], results)
        
        return results

    def bfs(self, end, distance, dict):
        distance[end] = 0
        queue = collections.deque([end])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)
    
    def dfs(self, word, target, distance, dict, path, results):
        if word == target:
            results.append(list(path))
            return
        
        for next_word in self.get_next_words(word, dict):
            if distance[next_word] != distance[word] - 1:    # 保证下一个单词距离end更近
                continue
            path.append(next_word)
            self.dfs(next_word, target, distance, dict, path, results)
            path.pop()

    def get_next_words(self, word, dict):
        next_words = []
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i + 1:]
                if next_word != word and next_word in dict:
                    next_words.append(next_word)
        return next_words
                        