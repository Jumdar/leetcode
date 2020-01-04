class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def search(nums, camp):
            if len(nums) == 0:
                res.append(camp)
                return
            for i in range(len(nums)):
                search(nums[:i] + nums[i+1:], camp + [nums[i]])

        search(nums, [])
        return res