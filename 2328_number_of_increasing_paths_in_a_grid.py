class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        MOD = (10**9)+7
        rows, cols = len(grid), len(grid[0])
        dp = [[1 for col in range(cols)] for row in range(rows)]
        arr = []  # val, row, col
        for row in range(rows):
            for col in range(cols):
                arr.append((grid[row][col], row, col))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isIncreasingCell(row, col, val, rows, cols):
            if row in range(0, rows) and col in range(0, cols) and grid[row][col] > val:
                return True
        res = rows*cols
        arr.sort()
        for val, row, col in arr:
            grid[row][col] = -1  # so we can never return
            for drow, dcol in directions:
                nrow = row+drow
                ncol = col + dcol
                if isIncreasingCell(nrow, ncol, val, rows, cols):
                    dp[nrow][ncol] = (dp[nrow][ncol] + dp[row][col]) % MOD
                    res = (res + dp[row][col]) % MOD
        return res


grid = [[1, 1], [3, 4]]
output = 8

obj = Solution()
res = obj.countPaths(grid)
print(res)
print(output)
print(res == output)
