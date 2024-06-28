from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda i: i[1] - i[0] + 1)
        res = []
        for query in queries:
            found = False
            for interval in intervals:
                if query in range(interval[0], interval[1]+1):
                    res.append(interval[1] - interval[0] + 1)
                    found = True
                    break
            if not found:
                res.append(-1)
        return res


intervals = [[1, 4], [2, 4], [3, 6], [4, 4]]
queries = [2, 3, 4, 5]
output = [3, 3, 1, 4]
obj = Solution()
res = obj.minInterval(intervals, queries)
print(res)
print(res == output)
