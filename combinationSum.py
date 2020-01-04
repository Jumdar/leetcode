class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        global result
        result = []

        def match(candidates, target, sum, camp):
            if sum == target:
                result.append(camp)
                return 0
            for i in range(len(candidates)):
                if candidates[i] + sum <= target:
                    camp.append(candidates[i])
                    match(candidates, target, sum, camp)
                else:
                    break
            return 0

        sorted(candidates)
        match(candidates, target, 0, [])

        return result

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """

    global result
    result = []

    def match(candidates, target, sum, camp):
        if sum == target:
            result.append(camp)
            return
        for i in range(len(candidates)):
            if candidates[i] + sum <= target:
                camp.append(candidates[i])
                match(candidates, target, sum, camp)
            else:
                break
        return

    sorted(candidates)
    match(candidates, target, 0, [])

    return result

if __name__ == '__main__':

    candidates = [2,3,6,7]
    target = 7
    print(combinationSum(candidates, target))