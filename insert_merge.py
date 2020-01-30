def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    intervals.append(newInterval)
    n = len(intervals)
    intervals = sorted(intervals, key=lambda x:x[0], reverse=False)
    tmp = [intervals[0]]
    for i in range(1, n):
        if tmp[-1][1] >= intervals[i][0]:
            tmp[-1][1] = max(tmp[-1][1], intervals[i][1])
        else:
            tmp.append(intervals[i])
    return tmp