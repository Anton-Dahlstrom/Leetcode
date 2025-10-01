from collections import defaultdict


class Solution:
    def minimumFuelCost(self, roads: list[list[int]], seats: int) -> int:
        edges = defaultdict(set)
        for f, t in roads:
            edges[f].add(t)
            edges[t].add(f)
        self.res = 0

        def dfs(prev, cur):
            people = 1
            for node in edges[cur]:
                if node != prev:
                    people += dfs(cur, node)
            if cur:
                self.res += people//seats
                if people % seats:
                    self.res += 1
                return people
        dfs(-1, 0)
        return self.res


roads = [[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]]
seats = 2
output = 7

obj = Solution()
res = obj.minimumFuelCost(roads, seats)
print(res)
print(output)
print(res == output)
