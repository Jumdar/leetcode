class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)

def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    sn = len(s)
    pn = len(p)
    dp = [[False] * (pn+1) for _ in range(sn+1)]
    dp[0][0] = True
    for i in range(pn-1):
        if p[i] == '*':
            dp[0][i+1] = dp[0][i]

    for i in range(1, sn+1):
        for j in range(1, pn+1):
            if s[i-1] == p[j-1] or p[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j+1]

    return dp[-1][-1]

if __name__ == '__main__':
    s = 'adceb'
    p = '*a*b'
    print(isMatch(s,p))