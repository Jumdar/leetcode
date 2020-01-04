# -*- coding:utf-8 -*-


class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) > 0:
            root = TreeNode(pre[0])
            root_id = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:root_id], tin[:root_id])
            root.right = self.reConstructBinaryTree(pre[root_id+1:], tin[root_id+1:])
            return root
