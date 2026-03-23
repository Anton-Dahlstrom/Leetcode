from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9+7
        rows, cols = len(grid), len(grid[0])
        neg = [[0]*cols for _ in range(rows)]
        pos = [[0]*cols for _ in range(rows)]
        neg[0][0] = grid[0][0]
        pos[0][0] = grid[0][0]
        zero = False
        for row in range(rows):
            for col in range(cols):
                cur = grid[row][col]
                if not cur:
                    zero = True
                if row+col == 0:
                    continue
                big = 0
                small = 0
                if row:
                    big = max(big, pos[row-1][col])
                    small = min(small, neg[row-1][col])
                if col:
                    big = max(big, pos[row][col-1])
                    small = min(small, neg[row][col-1])

                if cur > 0:
                    pos[row][col] = big * cur
                    neg[row][col] = small * cur
                else:
                    pos[row][col] = small * cur
                    neg[row][col] = big * cur
        res = pos[rows-1][cols-1] % MOD
        if not zero and not res:
            return -1
        return res
