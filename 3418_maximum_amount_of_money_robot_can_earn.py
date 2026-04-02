from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        rows, cols = len(coins), len(coins[0])
        dp = [[[0]*3 for col in range(cols)] for row in range(rows)]
        for i in range(rows):
            for j in range(cols):
                for k in range(3):
                    val = coins[i][j]
                    if i + j == 0:
                        dp[i][j][k] = val
                        if k:
                            dp[i][j][k] = max(0, dp[i][j][k-1])
                        continue
                    best = float("-inf")
                    if i:
                        best = max(best, dp[i-1][j][k] + val)
                        if k:
                            best = max(best, dp[i-1][j][k-1])
                    if j:
                        best = max(best, dp[i][j-1][k] + val)
                        if k:
                            best = max(best, dp[i][j-1][k-1])
                    dp[i][j][k] = best
        return dp[rows-1][cols-1][2]
