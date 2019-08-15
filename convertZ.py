class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        curRow = 0
        goingDown = False
        temp = [[] for i in range(numRows)]
        for j in range(len(s)):
            temp[curRow].append(s[j])
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown
            if goingDown:
                curRow += 1
            else:
                curRow += -1
        temp = [''.join(temp[i]) for i in range(numRows)]
        return ''.join(temp)
