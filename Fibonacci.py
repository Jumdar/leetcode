# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n <= 1:
            return n
        else:
            return (self.Fibonacci(n-1) + self.Fibonacci(n-2))
