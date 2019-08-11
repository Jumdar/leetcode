class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        medNum = (len(nums1)+len(nums2))/2
        temp = []
        i, j = 0, 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i<len(nums1) or j<len(nums2):
            if i<len(nums1):
                temp.append(nums1[i])
                i += 1
            if j<len(nums2):
                temp.append(nums2[j])
                j += 1
        if (len(nums1) + len(nums2)) % 2 != 0:
            result = temp[medNum]
        else:
            result = (temp[medNum-1]+temp[medNum])/2.0
        return result

