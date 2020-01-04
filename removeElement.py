def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    length = len(nums)
    i = 0
    while i < length:
        if nums[i] == val:
            nums.remove(val)
            length -= 1
        else:
            i += 1
    print(nums)
    return length

nums = [0,1,2,2,3,0,4,2]
val = 2

removeElement(nums, val)
