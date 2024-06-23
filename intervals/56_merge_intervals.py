from typing import List

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
Output = [[1, 6], [8, 10], [15, 18]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return
        intervals.sort()
        res = []
        temp = []
        prev = []
        for i in range(0, len(intervals)):
            cur = intervals[i]
            if not temp:
                temp = cur
                continue
            if cur[0] > temp[1]:
                res.append(temp)
                temp = cur
                continue
            if cur[0] < temp[0]:
                temp[0] = cur[0]
                temp[1] = max(cur[1], temp[1])
            elif cur[0] in range(temp[0], temp[1]+1):
                temp[1] = max(cur[1], temp[1])

        if temp:
            res.append(temp)
        return res


obj = Solution()
res = obj.merge(intervals)
print(res)
