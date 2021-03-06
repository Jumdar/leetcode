class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n and s not in ans:
                ans.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return ans

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []

    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n and s not in ans:
            ans.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)

    backtrack()
    return ans

if __name__ == '__main__':
    n = 3
    print(generateParenthesis(n))
