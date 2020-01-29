def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    res = []
    while matrix:
        res += matrix.pop(0)
        matrix = list(map(list, zip(*matrix)))[::-1]
    return res


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(matrix[::-1])
    matrix1 = zip(*matrix)
    matrix2 = list(map(list, matrix1))[::-1]
    print(matrix2)