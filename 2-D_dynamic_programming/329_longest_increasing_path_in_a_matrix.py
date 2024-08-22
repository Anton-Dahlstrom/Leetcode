class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:

        res = 0
        hmap = {}
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c):
            if (r, c) in hmap:
                return hmap[(r, c)] + 1
            longest = 0
            for y, x in directions:
                newR = r + y
                newC = c + x
                if (-1 < newR < len(matrix)) and (-1 < newC < len(matrix[0])) and matrix[r][c] < matrix[newR][newC]:
                    longest = max(longest, dfs(newR, newC))
            hmap[(r, c)] = longest
            return longest + 1

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res = max(res, dfs(r, c))

        return res


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
output = 4

obj = Solution()
res = obj.longestIncreasingPath(matrix)
print(res)
print(res == output)
