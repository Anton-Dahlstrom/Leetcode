class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        hmap = {}
        cap = float('inf')
        res = 0
        for i, char in enumerate(s):
            size = max(abs(points[i][0]), abs(points[i][1]))
            if char in hmap:
                cap = min(cap, max(hmap[char], size))
                hmap[char] = min(hmap[char], size)
            else:
                hmap[char] = size
        for char in hmap:
            if hmap[char] < cap:
                res += 1
        return res


points = [[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]]
s = "abdca"
output = 2


sol = Solution()
res = sol.maxPointsInsideSquare(points, s)
print(res)
print(res == output)
