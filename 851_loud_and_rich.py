from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        graph = defaultdict(set)
        for rich, poor in richer:
            graph[poor].add(rich)

        res = []
        for i in range(n):
            best = i
            cur = graph[i]
            visited = set()
            while cur:
                temp = set()
                for node in cur:
                    if quiet[node] < quiet[best]:
                        best = node
                    for edge in graph[node]:
                        if edge in visited:
                            continue
                        visited.add(edge)
                        temp.add(edge)
                cur = temp
            res.append(best)
        return res


richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
quiet = [3, 2, 5, 4, 6, 1, 7, 0]
output = [5, 5, 2, 5, 4, 5, 6, 7]

obj = Solution()
res = obj.loudAndRich(richer, quiet)
print(res)
print(output)
print(res == output)
