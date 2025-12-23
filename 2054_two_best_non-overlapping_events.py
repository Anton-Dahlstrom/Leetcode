class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        # look for the best second event to take
        # the highest value event that starts after event[i]
        # best event we can take for a given ending with lazy deletion
        stack = events.copy()
        stack.sort(key=lambda x: x[2])
        events.sort(key=lambda x: x[1])
        res = 0
        for start, end, value in events:
            while stack and stack[-1][0] <= end:
                stack.pop()
            if stack:
                value += stack[-1][2]
            res = max(res, value)

        return res


events = [[1, 3, 2], [4, 5, 2], [2, 4, 3]]
output = 4

obj = Solution()
res = obj.maxTwoEvents(events)
print(res)
print(output)
print(res == output)
