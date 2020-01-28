import copy
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    def backtrack():
        row = len(queens)  # 下标为行的索引
        if row == n:  # 若已有n个元素则满足要求
            output.append(queens[:])
        for col in range(n):  # 从第一行第一列开始遍历
            if col not in queens and xy_dif[row - col] and xy_sum[row + col]:  # 判断是否能放置棋子
                queens.append(col)  # 放置棋子
                xy_dif[row - col], xy_sum[row + col] = False, False
                backtrack()  # 向下一行探索
                queens.pop()  # 回溯，挪开棋子
                xy_dif[row - col], xy_sum[row + col] = True, True

    queens = []
    xy_dif = [True] * (2 * n - 1)
    xy_sum = [True] * (2 * n - 1)
    output = []  # 所有的结果集
    backtrack()  # 开始回溯
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in output]

if __name__ == '__main__':
    res = solveNQueens(4)
    print(res)