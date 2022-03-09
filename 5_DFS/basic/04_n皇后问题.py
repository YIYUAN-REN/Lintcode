# N-Queens

"""
˼·����������
ÿ���������壺n�㣬ÿ����������ĸ�λ��
ÿ����ٸ�״̬��n��״̬��n����ͬ��λ��

base case�����������һ�㣬����results
recursive rule������ǰλ��valid�����벢����һ��
"""

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        if n == 0:
            return []
        
        result = []
        self.dfs(n, [], result)
        return result
    
    
    def dfs(self, n, board, result):   # board��һά�����ʾ��ά����λ��: [2,5,3]��ʾ[(0,2), (1,5), (2,3)]
        # base case
        if len(board) == n:
            result.append(self.draw(board))
            return
        
        # recursion rule
        for col in range(n):
            if self.is_valid(col, board):
                board.append(col)
                self.dfs(n, board, results)
                board.pop()
    
    
    def is_valid(self, board, col):
        # row��col: ��ǰ���к���
        # r��c: ���ʹ����к���
        row = len(board)    # ��Ԫ�����ڵ�row
        for r in range(row):
            c = board[r]
            if col == c or abs(col - c) == row - r:  # ����ͬ��/б��(�в� = �в�)���򷵻�false
                return False
        return True
    
    
    def draw(self, board):
        new_board = []
        for col in board:
            row = ''.join(['Q' if c == col else '.' for c in range(len(board))])
            new_board.append(row)
        return new_board