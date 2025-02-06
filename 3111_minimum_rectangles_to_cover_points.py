class Solution:
    def minRectanglesToCoverPoints(self, points: list[list[int]], w: int) -> int:
        res = 1
        points.sort()
        cur = points[0][0]
        for p in points:
            x = p[0]
            if x in range(cur, cur+w+1):
                continue
            res += 1
            cur = x

        return res


points = [[2, 1], [1, 0], [1, 4], [1, 8], [3, 5], [4, 6]]
w = 1
output = 2

obj = Solution()
res = obj.minRectanglesToCoverPoints(points, w)
print(res)
print(output)
print(res == output)
