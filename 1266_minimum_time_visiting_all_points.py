class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        res = 0
        x, y = points[0]
        for newx, newy in points[1:]:
            xdiff = abs(x - newx)
            ydiff = abs(y - newy)
            res += max(xdiff, ydiff)
            x, y = newx, newy

        return res


points = [[1, 1], [3, 4], [-1, 0]]
output = 7

obj = Solution()
res = obj.minTimeToVisitAllPoints(points)
print(res)
print(output)
print(res == output)
