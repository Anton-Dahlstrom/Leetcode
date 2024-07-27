class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Creates wrong amount of connections and can create multiple paths.

        def calcDistance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        edges = {}

        for i in range(len(points)):
            edges[i] = []
            for j in range(len(points)):
                if i == j:
                    continue
                distance = calcDistance(points[i], points[j])
                edges[i].append([distance, j])
            edges[i].sort()

        res = 0

        # Need to check that all nodes are connected and don't loop.
        # Try to guarantee the first result is the smallest we can achieve.
        # If we can't guarantee return if tempres > res.

        def dfs(node):
            for point in edges[node]:
                dfs(point)
        dfs(0)
        print(edges)


points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
output = 20

points = [[2, -3], [-17, -8], [13, 8], [-17, -15]]
output = 53

obj = Solution()
res = obj.minCostConnectPoints(points)
print(res)
print(res == output)
