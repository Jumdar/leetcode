class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k, l = j + 1, len(nums) - 1
                while k < l:
                    temp = nums[i] + nums[j] + nums[k] + nums[l]
                    if temp == target:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif temp < target:
                        k += 1
                    elif temp > target:
                        l -= 1
        res = []
        for i in ans:
            res.append(list(i))

        return res


def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    ans = set()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            k, l = j + 1, len(nums) - 1
            while k < l:
                temp = nums[i] + nums[j] + nums[k] + nums[l]
                if temp == target:
                    ans.add((nums[i], nums[j], nums[k], nums[l]))
                    k += 1
                    l -= 1
                elif temp < target:
                    k += 1
                elif temp > target:
                    l -= 1
    res = []
    for i in ans:
        res.append(list(i))

    return res

if __name__ == '__main__':
    nums = [-3, -2, -1, 0, 0, 1, 2, 3]
    target = 0
    print(fourSum(nums, target))
