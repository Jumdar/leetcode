class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        res = [-1, -1]
        while left <= right:
            if nums[left] == target:
                res[0] = left
                break
            else:
                left += 1
        while left <= right:
            if nums[right] == target:
                res[1] = right
                break
            else:
                right -= 1

        return res
