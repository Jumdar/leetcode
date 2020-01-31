def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    arr = [x+1 for x in range(n*n)]
    matrix = [[0 for i in range(n)] for _ in range(n)]

    i, j = 0, 0
    while arr:
        while j < n and matrix[i][j] == 0:
            matrix[i][j] = arr[0]
            j += 1
            arr.pop(0)
        j -= 1
        i += 1
        while i < n and matrix[i][j] == 0:
            matrix[i][j] = arr[0]
            i += 1
            arr.pop(0)
        i -= 1
        j -= 1
        while j >= 0 and matrix[i][j] == 0:
            matrix[i][j] = arr[0]
            j -= 1
            arr.pop(0)
        j += 1
        i -= 1
        while i >= 0 and matrix[i][j] == 0:
            matrix[i][j] = arr[0]
            i -= 1
            arr.pop(0)
        i += 1
        j += 1

    return matrix


if __name__ == '__main__':
    res = generateMatrix(5)
    for r in res:
        print(r)