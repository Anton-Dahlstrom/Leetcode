class Solution:
    def maxPointsInsideSquare(self, points: list[list[int]], s: str) -> int:
        # After the largest size the square can be is found (the cap)
        # we need to loop through all the characters and see which fit.
        # For each that fit we add 1 to our result.
        hmap = {}
        size = 0
        cap = float('inf')
        for i, char in enumerate(s):
            s = min(abs(points[i][0]), abs(points[i][1]))
            l = max(abs(points[i][0]), abs(points[i][1]))
            if char in hmap:
                if hmap[char][1] < s:
                    cap = min(cap, s, hmap[char][1])
                elif hmap[char][0] > l:
                    cap = min(cap, hmap[char][0])
                    hmap[char][0] = [l]
            else:
                hmap[char] = [s, l]
                size = max(size, l)
        print(hmap)
        print(size, cap)
        return min(size, cap)


points = [[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]]
s = "abdca"
# 2

points = [[1, 1], [-1, -1], [2, -2]]
s = "ccd"
# 0


sol = Solution()
res = sol.maxPointsInsideSquare(points, s)
print(res)
