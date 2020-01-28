class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        set_row = [[], [], [], [], [], [], [], [], []]
        set_square = [[], [], []]
        for i in range(len(board[0])):
            if i % 3 == 0:
                set_square = [[], [], []]
            set_col = []
            for j in range(len(board)):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in set_row[j]:
                    set_row[j].append(board[i][j])
                else:
                    return False
                if board[i][j] not in set_col:
                    set_col.append(board[i][j])
                else:
                    return False
                if 0 <= j < 3:
                    if board[i][j] not in set_square[0]:
                        set_square[0].append(board[i][j])
                    else:
                        return False
                elif 3 <= j < 6:
                    if board[i][j] not in set_square[1]:
                        set_square[1].append(board[i][j])
                    else:
                        return False
                else:
                    if board[i][j] not in set_square[2]:
                        set_square[2].append(board[i][j])
                    else:
                        return False
        return True

