from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: list[list[int]]) -> list[int]:
        distinct = 0
        colors = defaultdict(int)
        balls = defaultdict(int)
        res = []
        for query in queries:
            ball, color = query
            if balls[ball] == color:
                res.append(distinct)
                continue
            if balls[ball] > 0:
                colors[balls[ball]] -= 1
                if colors[balls[ball]] == 0:
                    distinct -= 1
            balls[ball] = color
            if colors[balls[ball]] == 0:
                distinct += 1
            colors[balls[ball]] += 1
            res.append(distinct)
        return res


limit = 6
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
output = [1, 2, 2, 3, 4]

obj = Solution()
res = obj.queryResults(limit, queries)
print(res)
print(output)
print(res == output)
