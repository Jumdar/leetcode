import copy
def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = copy.deepcopy(nums)
    for i in range(1, n):
        if dp[i-1]+nums[i] > nums[i]:
            dp[i] = dp[i-1] + nums[i]

    return max(dp)

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxSubArray(nums))