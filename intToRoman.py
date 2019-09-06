class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        alphas = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        result = ''
        i = 0
        while i < len(nums):
            if nums[i] <= num:
                num = num - nums[i]
                result += alphas[i]
            else:
                i += 1

        return result

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    alphas = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    result = ''
    i = 0
    while i < len(nums):
        if nums[i] <= num:
            num = num - nums[i]
            result += alphas[i]
        else:
            i += 1

    return result

if __name__ == '__main__':
    num = 9
    print(intToRoman(num))