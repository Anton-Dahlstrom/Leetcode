class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [set() for _ in range(cols)]
        dp[0] = {grid[0][0]}
        for col in range(1, cols):
            cur = grid[0][col]
            for num in dp[col-1]:
                dp[col].add(cur ^ num)

        for row in range(1, rows):
            temp = [set() for _ in range(cols)]
            for col in range(cols):
                cur = grid[row][col]
                for num in dp[col]:
                    temp[col].add(cur ^ num)
                if col:
                    for num in temp[col-1]:
                        temp[col].add(cur ^ num)
            dp = temp

        return min(dp[-1])
