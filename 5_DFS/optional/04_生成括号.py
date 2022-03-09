# Generate Parentheses

"""
ÿ���������壺2n�㣬ÿ�������'('���Ǽ�')'
ÿ����ٸ�״̬��2��״̬����'('�ͼ�')'

base case: ��������index = ������index = n������results
recursive rule:
    case 1: ��������index < n����'('����
    case 2: ��������index < ������index����')'����
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
            self.dfs(n, l + 1, r, prefix + "(", results)	# ��prefix��list��Ҫ��recursionǰ��append��pop
        
        if r < l:
            self.dfs(n, l, r + 1, prefix + ")", results)