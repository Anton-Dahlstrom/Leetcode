class Solution:
    def numberOfRoutes(self, grid: list[str], d: int) -> int:
        MOD = 10**9+7
        rows, cols = len(grid), len(grid[0])
        dp = [1 if grid[rows-1][col] == "." else 0 for col in range(cols)]

        def fillRow(row, arr, dist):
            adding = [0]*cols
            cur = 0
            r = 0
            while r < dist and r < cols:
                cur += arr[r]
                r += 1
            for col in range(cols):
                if col+dist < cols:
                    cur += arr[col+dist]
                if col-dist-1 >= 0:
                    cur -= arr[col-dist-1]
                adding[col] = cur % MOD
                if grid[row][col] != ".":
                    adding[col] = 0
            return adding

        dp = [1 if grid[rows-1][col] == "." else 0 for col in range(cols)]
        for row in range(rows-1, 0, -1):
            dp = fillRow(row, dp, d)
            dp = fillRow(row-1, dp, d-1)
        dp = fillRow(0, dp, d)
        return sum(dp) % MOD


grid = ["..", "#."]
d = 2
output = 4


obj = Solution()
res = obj.numberOfRoutes(grid, d)
print(res)
print(output)
print(res == output)
