# Generate Parentheses

"""
每层代表的意义：2n层，每层决定加'('还是加')'
每层多少个状态：2个状态，加'('和加')'

base case: 若左括号index = 右括号index = n，放入results
recursive rule:
    case 1: 若左括号index < n，加'('括号
    case 2: 若右括号index < 左括号index，加')'括号
"""

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        results = []
        self.dfs(n, 0, 0, "", results)
        return results
    
    
    def dfs(self, n, l, r, prefix, results):
        if l == n and r == n:
            results.append(prefix)
            return
        
        if l < n:
            self.dfs(n, l + 1, r, prefix + "(", results)	# 若prefix是list，要在recursion前后append和pop
        
        if r < l:
            self.dfs(n, l, r + 1, prefix + ")", results)