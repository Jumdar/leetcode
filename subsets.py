import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        """
            :type nums: List[int]
            :rtype: List[List[int]]
            """

        result = []
        n = len(nums)

        def merge(i, tmp):
            result.append(tmp)
            for j in range(i, n):
                merge(j + 1, tmp + [nums[j]])

        merge(0, [])

        return result

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    n = len(nums)

    def merge(i, tmp):
        result.append(tmp)
        for j in range(i, n):
            merge(j+1, tmp + [nums[j]])

    merge(0, [])

    return result


if __name__ == '__main__':
    nums = [3,2,1,4]
    result = subsets(nums)
    print(result)
