# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        visited = [False] * len(matrix)
        pos = 0
        res = False
        for i in range(rows):
            for j in range(cols):
                res = self.search(matrix, rows, cols, i, j, path, pos, visited)
        return res

    def search(self, matrix, rows, cols, i, j, path, pos, visited):
        if pos == len(path):
            return True

        res = False
        if 0 <= i < rows and 0 <= j < cols and \
                matrix[i][j] == path[pos] and visited[j * cols + i] == False:

            visited[j * cols + i] = True
            res = self.search(matrix, rows, cols, i-1, j, path, pos+1, visited) or \
                self.search(matrix, rows, cols, i+1, j, path, pos+1, visited) or \
                self.search(matrix, rows, cols, i, j-1, path, pos+1, visited) or \
                self.search(matrix, rows, cols, i, j+1, path, pos+1, visited)
            if not res:
                visited[j * cols + i] = False
                pos -= 1

        return res