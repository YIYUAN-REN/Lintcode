# N-Queens

"""
思路：排列问题
每层代表的意义：n层，每层决定放在哪个位置
每层多少个状态：n个状态，n个不同的位置

base case：若放完最后一层，放入results
recursive rule：若当前位置valid，放入并到下一层
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
    
    
    def dfs(self, n, board, result):   # board用一维数组表示二维矩阵位置: [2,5,3]表示[(0,2), (1,5), (2,3)]
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
        # row和col: 当前的行和列
        # r和c: 访问过的行和列
        row = len(board)    # 新元素所在的row
        for r in range(row):
            c = board[r]
            if col == c or abs(col - c) == row - r:  # 若在同列/斜线(列差 = 行差)，则返回false
                return False
        return True
    
    
    def draw(self, board):
        new_board = []
        for col in board:
            row = ''.join(['Q' if c == col else '.' for c in range(len(board))])
            new_board.append(row)
        return new_board