# -*- coding:utf-8 -*-
import numpy as np
class Solution:

    def loc_sum(self, x):
        sum = 0
        while(x >= 0):
            a = x%10
            x = int(x/10)
            sum += a
        return sum

    def movingCount(self, threshold, rows, cols):
        visited = [False] * (rows * cols)
        res = self.search(threshold, rows, cols, 0, 0, visited)
        return res

    def search(self, thershold, rows, cols, i, j, visited):
        count = 0
        if 0 <= i < rows and 0 <= j < cols and self.loc_sum(i) + self.loc_sum(j) < thershold:
            visited[j*cols + i] = True
            count = 1 + self.search(thershold, rows, cols, i-1, j, visited) + \
                    self.search(thershold, rows, cols, i + 1, j, visited) + \
                    self.search(thershold, rows, cols, i, j - 1, visited) + \
                    self.search(thershold, rows, cols, i, j + 1, visited)

        return count
