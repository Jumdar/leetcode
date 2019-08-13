class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        result = ""
        if x>0:
            iter_num = len(s)
        else:
            iter_num = len(s)-1
        isHead = True
        for i in range(iter_num):
            if s[len(s)-i-1] == "0" and isHead:
                continue
            else:
                isHead = False
                result = result + s[len(s)-i-1]

        if x > 0:
            return int(result) if -2147483648 < x < 2147483647 else 0
        else:
            return int(s[0]+result) if -2147483648 < x < 2147483647 else 0