class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1]*n + [[1] + [0]*(n-1) for _ in range(m-1)]

        for i in range(m-1):
            for j in range(n-1):
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]

        return dp[-1][-1]

