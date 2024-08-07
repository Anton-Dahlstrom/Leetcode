from typing import List

intervals = [[1, 5], [5, 7], [9, 10]]
intervals = [[1, 5], [5, 7], [6, 10]]


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        def checkOverlap(interval1, interval2):
            if interval1[0] >= interval2[1] or interval2[0] >= interval1[1]:
                return False
            return True

        for i in range(0, len(intervals)-1):
            if checkOverlap(intervals[i], intervals[i+1]):
                return False
        return True


obj = Solution()
res = obj.canAttendMeetings(intervals)
print(res)
