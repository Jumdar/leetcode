# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return False
        else:
            return self.isSubTree(pRoot1, pRoot2)

    def isSubTree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return pRoot1 == pRoot2
        res = False
        if pRoot1.val == pRoot2.val:
            res = self.isSubTree(pRoot1.left, pRoot2.left) and self.isSubTree(pRoot1.right, pRoot2.right)
        else:
            res = self.isSubTree(pRoot1.left, pRoot2) or self.isSubTree(pRoot2.right, pRoot2)
        return res