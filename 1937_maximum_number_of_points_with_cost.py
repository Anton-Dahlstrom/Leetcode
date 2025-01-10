class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        for r in range(len(points)-1):
            temp = [0] * len(points[0])
            best = 0
            for c in range(len(points[0])):
                best = max(points[r][c], best-1)
                temp[c] = best
            best = temp[-1]
            for c in range(len(points[0])-1, -1, -1):
                best = max(points[r][c], best-1)
                points[r+1][c] += max(temp[c], best)
        return max(points[-1])


points = [[0, 3, 0, 4, 2], [5, 4, 2, 4, 1], [5, 0, 0, 5, 1], [2, 0, 1, 0, 3]]
output = 15

obj = Solution()
res = obj.maxPoints(points)
print(res)
print(output)
print(res == output)
