from typing import List

intervals = [[1, 5], [5, 7], [9, 10]]
intervals = [[1, 5], [5, 7], [6, 10]]


class Solution:
    def method(self, intervals: List[List[int]]) -> int:
        def checkOverlap(interval1, interval2):
            if interval1[0] >= interval2[1] or interval2[0] >= interval1[1]:
                return False
            if interval1[1] <= interval2[0] or interval2[1] <= interval1[0]:
                return False
            return True
        for i in range(0, len(intervals)-1):
            for j in range(i+1, len(intervals)):
                if checkOverlap(intervals[i], intervals[j]):
                    return False
        return True


obj = Solution()
res = obj.method(intervals)
print(res)
