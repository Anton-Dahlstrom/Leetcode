class Solution:
    def countDays(self, days: int, meetings: list[list[int]]) -> int:
        n = len(meetings)
        events = [0] * (n*2)
        for i in range(n):
            start, end = meetings[i]
            events[i] = (start, 1)
            events[i+n] = (end+1, -1)
        events.sort()

        res = 0
        meetingCount = 0
        prevDay = 1
        for i in range(len(events)):
            day, event = events[i]
            if day > days:
                break
            if not meetingCount:
                res += day-prevDay
            prevDay = day
            meetingCount += event
        if days >= day:
            res += days-prevDay+1
        return res


days = 10
meetings = [[5, 7], [1, 3], [9, 10]]
output = 2


days = 5
meetings = [[2, 4], [1, 3]]
output = 1

obj = Solution()
res = obj.countDays(days, meetings)
print(res)
print(output)
print(res == output)
