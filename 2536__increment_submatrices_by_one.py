class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        grid = [[0]*n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            grid[r1][c1] += 1
            if c2 < n-1:
                grid[r1][c2+1] -= 1
            if r2 < n-1:
                grid[r2+1][c1] -= 1
            if r2 < n-1 and c2 < n-1:
                grid[r2+1][c2+1] += 1

        for row in range(n):
            cur = 0
            for col in range(n):
                if row < n-1:
                    grid[row+1][col] += grid[row][col]
                cur += grid[row][col]
                grid[row][col] = cur

        return grid


n = 3
queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
output = [[1, 1, 0], [1, 2, 1], [0, 1, 1]]

obj = Solution()
res = obj.rangeAddQueries(n, queries)
print(res)
print(output)
print(res == output)
