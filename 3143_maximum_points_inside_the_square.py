from typing import List


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        hmap = {}
        size = 0
        cap = float('inf')
        for i, char in enumerate(s):
            s = min(abs(points[i][0]), abs(points[i][1]))
            l = max(abs(points[i][0]), abs(points[i][1]))
            if char in hmap:
                if hmap[char][1] < s:
                    cap = s
                elif hmap[char][0] > l:
                    cap = hmap[char][0]
                    hmap[char] = [s, l]

            else:
                hmap[char] = [s, l]
                size = max(size, l)

        return min(size, cap)


points = [[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]]
s = "abdca"
# 2

# points = [[1, 1], [-1, -1], [2, -2]]
# s = "ccd"
# # 0


sol = Solution()
res = sol.maxPointsInsideSquare(points, s)
print(res)
