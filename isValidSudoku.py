class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        set_col = [ [], [], []]
        for i in range(0, 9, 3): # 控制列
            set_row = [[], [], []]
            set_grid = [[], [], []]
            for j in range(9): # 控制行
                if board[j][i] != '.' and board[j][i] not in set_row[0] : # 第一列
                    set_row[0].append(board[j][i])

                if board[j][i+1] != '.' and board[j][i] not in set_row[1]:
                    set_row[1].append(board[j][i+1])

                if board[j][2] != '.' and board[j][i] not in set_row[2]:
                    set_row[2].append(board[j][i+2])

