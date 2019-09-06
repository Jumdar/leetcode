class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        result = 0
        i = len(s) - 1
        while i >= 0:
            temp = ''
            if i > 0:
                if (s[i] == 'V' and s[i - 1] == 'I') or (s[i] == 'X' and s[i - 1] == 'I') \
                        or (s[i] == 'L' and s[i - 1] == 'X') or (s[i] == 'C' and s[i - 1] == 'X') \
                        or (s[i] == 'D' and s[i - 1] == 'C') or (s[i] == 'M' and s[i - 1] == 'C'):
                    temp = s[i - 1] + s[i]
                    i -= 2
                else:
                    temp = s[i]
                    i -= 1
            else:
                temp = s[i]
                i -= 1
            result += dict[temp]
        return result


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict = {
        'I': 1,
        'IV': 4,
        'V': 5,
        'IX': 9,
        'X': 10,
        'XL': 40,
        'L': 50,
        'XC': 90,
        'C': 100,
        'CD': 400,
        'D': 500,
        'CM': 900,
        'M': 1000
    }
    result = 0
    i = len(s) - 1
    while i >= 0:
        temp = ''
        if i > 0:
            if (s[i] == 'V' and s[i - 1] == 'I') or (s[i] == 'X' and s[i - 1] == 'I') \
                    or (s[i] == 'L' and s[i - 1] == 'X') or (s[i] == 'C' and s[i - 1] == 'X') \
                    or (s[i] == 'D' and s[i - 1] == 'C') or (s[i] == 'M' and s[i - 1] == 'C'):
                temp = s[i - 1] + s[i]
                i -= 2
            else:
                temp = s[i]
                i -= 1
        else:
            temp = s[i]
            i -= 1
        result += dict[temp]
    return result

if __name__ == '__main__':
    s = 'MCMXCIV'
    print(romanToInt(s))