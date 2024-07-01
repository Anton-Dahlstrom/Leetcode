from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> int:

        def checkOverlap(interval1, interval2):
            if interval1.start >= interval2.end or interval2.start >= interval1.end:
                return False
            if interval1.end <= interval2.start or interval2.end <= interval1.start:
                return False
            return True

        for i in range(0, len(intervals)-1):
            if checkOverlap(intervals[i], intervals[i+1]):
                return False
        return True
