from collections import defaultdict


class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        res = [0]*n
        edges = defaultdict(set)
        for n1, n2 in paths:
            edges[n1].add(n2)
            edges[n2].add(n1)
        for i in range(n):
            conn = set()
            for node in edges[i+1]:
                conn.add(res[node-1])
            for garden in range(1, 5):
                if garden not in conn:
                    res[i] = garden
                    break
        return res


n = 4
paths = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]
output = [1, 2, 3, 4]

obj = Solution()
res = obj.gardenNoAdj(n, paths)
print(res)
print(output)
print(res == output)
