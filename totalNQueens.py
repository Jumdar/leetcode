def totalNQueens(n):
    """
    :type n: int
    :rtype: int
    """
    quenens = []
    xy_dif = [True] * (2 * n - 1)
    xy_sum = [True] * (2 * n - 1)
    output = []
    def backtrack():
        row = len(quenens)
        if row == n:
            output.append(quenens)
        for col in range(n):
            if col not in quenens and xy_dif[row-col] and xy_sum[row+col]:
                quenens.append(col)
                xy_dif[row-col], xy_sum[row+col] = False, False
                backtrack()
                quenens.pop()
                xy_dif[row-col], xy_sum[row+col] = True, True
    backtrack()
    result = [['.' * i + 'Q' + '.' * (n-i-1) for i in sol] for sol in output]
    return len(result)
