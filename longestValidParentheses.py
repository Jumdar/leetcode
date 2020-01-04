class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                if len(stack) > count:
                    count = len(stack)
            else:
                if len(stack) != 0:
                    stack.pop()
                else:
                    continue

        return count-len(stack)