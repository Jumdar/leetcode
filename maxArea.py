class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j and i < len(height) and j >= 0:
            temp = (j - i) * min(height[i], height[j])
            if temp > max_area:
                max_area = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i, j = 0, len(height)-1
    max_area = 0
    while i<j and i<len(height) and j>=0:
        temp = (j-i)*min(height[i], height[j])
        if temp > max_area:
            max_area = temp
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
