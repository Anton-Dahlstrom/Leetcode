class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
output = 11


obj = Solution()
res = obj.minimumTotal(triangle)
print(res)
print(output)
print(res == output)
