class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=1
        while(i<len(nums)-1):
            if nums[i] < nums[i+1]:
                break
            i+=1
        if i == len(nums)-1:
            for k in range(int(len(nums)/2)):
                tmp = nums[k]
                nums[k] = nums[len(nums)-k-1]
                nums[len(nums)-k-1] = tmp
        else:
            j=i+1
            while(j<len(nums)-1):
                if nums[j] > nums[j+1]:
                    break

            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

            for k in range(i, int((len(nums)-i)/2) + i ):
                tmp = nums[k]
                nums[k] = nums[len(nums) - k - 1]
                nums[len(nums) - k - 1] = tmp

        return nums

