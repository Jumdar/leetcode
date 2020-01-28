def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    res = []
    for i in range(n):
        tmp = []
        res.append(tmp)
    for i in range(n):
        for j in range(n):
            res[j].append(matrix[n - i - 1][j])
    # print(res)
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
res = rotate(matrix)
print(res)