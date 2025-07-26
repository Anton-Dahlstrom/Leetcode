class Solution:
    def maximumSumOfHeights(self, heights: list[int]) -> int:
        n = len(heights)
        bricks = sum(heights)
        res = 0
        for i in range(n):
            temp = bricks
            prev = heights[i]
            for j in range(i-1, -1, -1):
                temp -= max(0, heights[j] - prev)
                prev = min(heights[j], prev)
            prev = heights[i]
            for j in range(i+1, n):
                temp -= max(0, heights[j] - prev)
                prev = min(heights[j], prev)
            res = max(res, temp)
        return res


heights = [6, 5, 3, 9, 2, 7]
output = 22

obj = Solution()
res = obj.maximumSumOfHeights(heights)
print(res)
print(output)
print(res == output)
