from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        print([[interval.start, interval.end] for interval in intervals])
        intervals.sort(key=lambda i: i.start)
        res = []
        for inter in intervals:
            append = False
            for merged in res:
                if inter.start >= merged.end:
                    merged.end = inter.end
                    append = True
                    break
            if not append:
                res.append(inter)
        return len(res)


intervals = [(0, 40), (5, 10), (15, 20)]
output = 2

intervals = [Interval(l, r) for l, r in intervals]
obj = Solution()
res = obj.minMeetingRooms(intervals)
print(res)
print(res == output)
