class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = list(str(x))
        tag = True
        for i in range(len(temp)/2):
            if temp[i] == temp[len(temp)-i-1]:
                continue
            else:
                tag = False
        return tag