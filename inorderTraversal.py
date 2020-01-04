# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [(False, root)]
        res = []
        while stack:
            isvisted, node = stack.pop()
            if not isvisted:
                stack.append((False, node.right))
                stack.append((True, node))
                stack.append((False, node.left))
            else:
                res.append(node.val)
        return res