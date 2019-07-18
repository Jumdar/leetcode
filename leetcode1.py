class Solution:
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)):
            temp = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == temp:
                    result.append(i)
                    result.append(j)

        return result