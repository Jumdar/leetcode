class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        i, j = 0, 0
        rows = len(board)
        cols = len(board[0])
        flag = True
        for k in range(len(word)):
            if i < rows and board[i + 1][j] == word[k]:
                board[i + 1][j] = True
            elif i > 0 and board[i - 1][j] == word[k]:
                board[i - 1][j] = True
            elif j < cols and board[i][j + 1] == word[k]:
                board[i][j + 1] = True
            elif j > 0 and board[i][j - 1] == word[k]:
                board[i][j - 1] = True
            else:
                flag = False
                break;

        return flag


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    rows = len(board)-1
    cols = len(board[0])-1
    flag = False
    start = []
    for m in range(rows+1):
        for n in range(cols+1):
            if board[m][n] == word[0]:
                flag = True
                start.append((m, n))
    print(start)
    result = []
    if flag:
        for s in start:
            flag = True
            i, j = s[0], s[1]
            k = 1
            while k < len(word):
                print("{}, {}".format(i, j))
                if i < rows and board[i + 1][j] == word[k]:
                    board[i + 1][j] = True
                    i += 1
                        #print('yes')
                elif i > 0 and board[i - 1][j] == word[k]:
                    board[i - 1][j] = True
                    i -= 1
                        #print('yes')
                elif j < cols and board[i][j + 1] == word[k]:
                    board[i][j + 1] = True
                    j += 1
                        #print('yes')
                elif j > 0 and board[i][j - 1] == word[k]:
                    board[i][j - 1] = True
                    j -= 1
                        #print('yes')
                else:
                    flag = False
                    break
                k += 1
            result.append(flag)

    print(result)
    if True in result:
        return True
    else:
        return False

if __name__ == '__main__':
    board = [
        ["a","a"]
    ]
    word = "aaa"
    print(board[0][0] == word[0])
    print(exist(board, word))
