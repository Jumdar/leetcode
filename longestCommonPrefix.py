class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        str1 = strs[0]
        str2 = strs[1]
        i = 0
        str = ''
        while i < len(str1) and i < len(str2):
            if str1[i] == str2[i]:
                str += str1[i]
                i += 1
            else:
                break
        strs[1] = str
        return self.longestCommonPrefix(strs[1:])


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    print(strs)
    if len(strs) == 0:
        print("长度为0")
        return ''
    if len(strs) == 1:
        print("长度为1")
        return strs[0]
    str1 = strs[0]
    str2 = strs[1]
    i = 0
    str = ''
    while i < len(str1) and i < len(str2):
        print(i)
        if str1[i] == str2[i]:
            str += str1[i]
            i += 1
        else:
            break
    strs[1] = str
    return longestCommonPrefix(strs[1:])

if __name__ == '__main__':
    strs = ["aaa","aa","aaa"]
    result = longestCommonPrefix(strs)
    print(result)