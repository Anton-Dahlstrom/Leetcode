from typing import List

intervals = [[0,5],[9,12]]
newInterval = [7,16]


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        res = []
        temp = []
        i = 0
        if newInterval[0] < intervals[0][0]:
            temp.append(newInterval[0])

        else:
            for i, interval in enumerate(intervals):
                if newInterval[0] in range(interval[0], interval[1]+1):
                    temp.append(interval[0])
                    break
                elif newInterval[0] > interval[1]:
                    res.append(interval)
                else:
                    temp.append(newInterval[0])
                    break

        if not temp:
            return intervals

        if newInterval[1] > intervals[-1][1]:
            temp.append(newInterval[1])
            res.append(temp)
            return res

        for j in range(i, len(intervals)):
            if newInterval[1] < intervals[j][0]:
                temp.append(newInterval[1])
                res.append(temp)
                res.append(intervals[j])
                break

            if newInterval[1] in range(intervals[j][0], intervals[j][1]+1):
                temp.append(intervals[j][1])
                res.append(temp)
                break

        for k in range(j+1, len(intervals)):
            res.append(intervals[k])
        return res

obj = Solution()
res = obj.insert(intervals, newInterval)
print(res)