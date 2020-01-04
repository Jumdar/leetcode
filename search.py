class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1

        while left <= right:

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            judge1 = nums[left] < nums[mid] and nums[left] <= target and nums[mid] > target
            judge2 = nums[left] > nums[mid] and (nums[left] <= target or nums[mid] > target)

            if judge1 or judge2:
                right = mid - 1
            else:
                left = mid + 1

        return -1