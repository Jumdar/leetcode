class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        list = []
        for i in range(len(str)):
            if str[i] is not ' ':
                list.append(str[i])
        temp = 0
        if len(list) is 0:
            return 0
        if list[0] < '0' or list[0] > '9':
            if list[0] is not '-':
                return 0
        count = 0
        for j in range(len(list)):
            if list[len(list) - j - 1] is '-':
                temp = -temp
                break
            if '0' <= list[len(list) - j - 1] <= '9':
                temp += int(list[len(list) - j - 1]) * pow(10, count)
                count += 1
        print(temp)
        if temp <= -pow(2, 31):
            temp = -pow(2, 31)
        if temp >= pow(2, 31) - 1:
            temp = pow(2, 31) - 1
        return temp

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    list = []
    for i in range(len(str)):
        if str[i] is not ' ':
            list.append(str[i])
    temp = 0
    if len(list) is 0:
        return 0
    if list[0] < '0' or list[0] > '9' :
        if list[0] is not '-':
            return 0
    count = 0
    for j in range(len(list)):
        if list[len(list)-j-1] is '-':
            temp = -temp
            break
        if '0'<=list[len(list)-j-1]<='9':
            temp += int(list[len(list)-j-1])*pow(10,count)
            count += 1
    print(temp)
    if temp<=-pow(2,31):
        temp = -pow(2,31)
    if temp>=pow(2,31)-1:
        temp = pow(2,31)-1
    return temp

if __name__ == '__main__':
    str = "    -42"
    print(myAtoi(str))