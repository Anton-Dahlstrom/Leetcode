class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(i+2, n):
                    p1, p2, p3 = points[i], points[j], points[k]
                    x1, y1 = p1
                    x2, y2 = p2
                    x3, y3 = p3
                    size = abs((x1 * (y2-y3)) +
                               (x2 * (y3-y1)) + (x3 * (y1 - y2)))/2
                    size = round(size, 5)
                    res = max(res, size)

        return res


points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
output = 2.00000

obj = Solution()
res = obj.largestTriangleArea(points)
print(res)
print(output)
print(res == output)
