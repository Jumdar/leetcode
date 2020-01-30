def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(intervals)
    if n == 0:
        return []
    intervals = sorted(intervals, key=lambda x:x[0], reverse=False)
    tmp = [intervals[0]]
    for i in range(1, n):
        if tmp[-1][1] > intervals[i][0]:
            tmp[-1][1] = max(tmp[-1][1], intervals[i][1])
        else:
            tmp.append(intervals[i])
    return tmp

if __name__ == '__main__':
    intervals = [[1,4],[2,3]]
    print(merge(intervals))