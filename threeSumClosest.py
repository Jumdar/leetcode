class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res, min = 0, float('inf')
        for k in range(len(nums) - 2):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i, j = k + 1, len(nums) - 1
            while i < j:
                sum = nums[k] + nums[i] + nums[j]
                if abs(sum - target) < min:
                    min = abs(sum - target)
                    res = sum
                if sum > target:
                    j -= 1
                elif sum < target:
                    i += 1
                else:
                    return target
        return res

def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) < 3:
        return []
    nums.sort()
    res, min = 0, float('inf')
    for k in range(len(nums)-2):
        if k>0 and nums[k] == nums[k-1]:
            continue
        i, j = k+1, len(nums)-1
        while i < j:
            sum = nums[k] + nums[i] + nums[j]
            if abs(sum-target) < min:
                min = abs(sum-target)
                res = sum
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return target
    return res
if __name__ == '__main__':
    nums = [0, 1, 2]
    target = 1
    print(threeSumClosest(nums, target))