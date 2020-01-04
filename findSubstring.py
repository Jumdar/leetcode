class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        def match(s, words):
            stride = len(words[0])
            for i in range(len(s), stride):
                if s[i:i+3] in words:
                    words.pop(words.index(s[i:i+3]))
            if len(words) == 0:
                return True
            else:
                return False
        result = []

        for i in range(len(s)):
            res = match(s[i:], words)
            if res:
                result.append(i)
        return result

import copy
def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """

    def match(s, words):
        stride = len(words[0])
        for i in range(0, len(s), stride):
            if (i+3) > len(s):
                break
            if s[i:i + 3] in words:
                words.pop(words.index(s[i:i + 3]))
            else:
                break
        if len(words) == 0:
            return True
        else:
            return False

    result = []
    tmp = copy.deepcopy(words)
    for i in range(len(s)):
        res = match(s, words)
        if res:
            result.append(i)
        words = copy.deepcopy(tmp)

    return result

if __name__ == '__main__':

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    res = findSubstring(s, words)
    print(res)
