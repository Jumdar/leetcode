def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    def calShiftMat(needle):
        dic = {}
        for i in range(len(needle)-1, -1, -1):
            if not dic.get(needle[i]):
                dic[needle[i]] = len(needle)-i
        dic['ot'] = len(needle) + 1
        return dic

    if len(needle) > len(haystack):
        return -1
    if needle == '': return 0

    dic = calShiftMat(needle)
    idx = 0

    while idx+len(needle) <= len(haystack):
        str_cut = haystack[idx:idx+len(needle)]

        if str_cut == needle:
            return idx
        else:
            if idx+len(needle) >= len(haystack):
                return -1
            cur_c = haystack[idx+len(needle)]
            if dic.get(cur_c):
                idx += dic[cur_c]
            else:
                idx += dic['ot']

    return -1 if idx+len(needle) >= len(haystack) else idx