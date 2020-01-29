def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    start = 0
    end = 0
    n = len(nums)
    while start <= end and end < n - 1:
        end = max(end, nums[start] + start)
        start += 1
    return end >= n - 1