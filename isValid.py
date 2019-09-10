class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in mapping:
                if len(stack) > 0:
                    top_element = stack.pop()
                else:
                    return False
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)
        return not stack


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            if len(stack) > 0:
                top_element = stack.pop()
            else:
                return False
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

if __name__ == '__main__':
    s = "]"
    print(isValid(s))
