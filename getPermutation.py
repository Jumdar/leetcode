def getPermutation(n, k):
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n*factorial(n-1)
    def dfs(remian, s, n, k):
        if n == 1:
            return s + remian[0]
        div = factorial(n-1)
        ind = k // div
        k = k % div
        return dfs(remian[:ind]+remian[ind+1:], s+remian[ind], n-1, k)

    return dfs([str(x+1) for x in range(n)], '', n, k-1)

