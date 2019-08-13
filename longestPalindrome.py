class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_length = 0
        start = 0
        end = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if max_length < j - i + 1:
                        max_length = j - i + 1
                        start = i
                        end = j
        result = s[start:end + 1]
        return result