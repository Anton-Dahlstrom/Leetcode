from collections import defaultdict
from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        MOD = 10**12
        rows, cols = len(grid), len(grid[0])
        rowsum = [0] * rows
        rowmod = [0] * rows
        cnt = defaultdict(int)
        for row in range(rows-1, -1, -1):
            for col in range(cols):
                num = grid[row][col]
                rowsum[row] += num
                rowmod[row] += rowsum[row]//MOD
                rowsum[row] %= MOD
                if row == rows-1 and col in range(1, cols-1):
                    continue
                cnt[num] += 1
            if row:
                rowsum[row-1] += rowsum[row]
                rowmod[row-1] += rowmod[row]
        hset = set()
        colsum = 0
        colmod = 0
        for row in range(rows-1):
            for col in range(cols):
                num = grid[row][col]
                colsum += num
                colmod += colsum//MOD
                colsum %= MOD
                cnt[num] -= 1
                hset.add(num)
            if cols == 1:
                if colsum == rowsum[row+1]:
                    return True
                if rows > 2:
                    # cut first
                    if colsum - grid[0][0] == rowsum[row+1]:
                        return True
                    # cut last
                    if colsum == rowsum[row+1] - rowsum[rows-1]:
                        return True
                    # cut between
                    if row < rows-2 and colsum == rowsum[row+2]:
                        return True
                continue
            if colmod > rowmod[row+1]:
                colmod -= 1
                colsum += MOD
            if rowmod[row+1] > colmod:
                rowmod[row+1] -= 1
                rowsum[row+1] += MOD
            if rowmod[row+1] == colmod:
                if colsum == rowsum[row+1]:
                    return True
                if colsum - rowsum[row+1] in hset:
                    if row or colsum - rowsum[row+1] in (grid[0][0], grid[0][-1]):
                        return True
                if cnt[rowsum[row+1] - colsum] > 0:
                    if row < rows-1 or rowsum[row+1] - colsum in (grid[rows-1][0], grid[rows-1][-1]):
                        return True

        colsum = [0] * cols
        colmod = [0] * cols
        cnt = defaultdict(int)
        for col in range(cols-1, -1, -1):
            for row in range(rows):
                num = grid[row][col]
                colsum[col] += num
                colmod[col] += colsum[col]//MOD
                colsum[col] %= MOD
                cnt[num] += 1
            if col:
                colsum[col-1] += colsum[col]
                colmod[col-1] += colmod[col]
        hset = set()
        rowsum = 0
        rowmod = 0
        for g in grid:
            print(g)
        for col in range(cols-1):
            for row in range(rows):
                num = grid[row][col]
                rowsum += num
                rowmod += rowsum//MOD
                rowsum %= MOD
                cnt[num] -= 1
                if not col and row in range(1, rows-1):
                    continue
                hset.add(num)
            if rows == 1:
                if rowsum == colsum[col+1]:
                    return True
                if cols > 2:
                    # cut first
                    if rowsum - grid[0][0] == colsum[col+1]:
                        return True
                    # cut last
                    if rowsum == colsum[col+1] - colsum[cols-1]:
                        return True
                    # cut between
                    if col < cols-2 and rowsum == colsum[col+2]:
                        return True
                continue

            if rowmod > colmod[col+1]:
                rowmod -= 1
                rowsum += MOD
            if colmod[col+1] > rowmod:
                colmod[col+1] -= 1
                colsum[col+1] += MOD
            if colmod[col+1] == rowmod:
                if rowsum == colsum[col+1]:
                    return True
                if rowsum - colsum[col+1] in hset:
                    if col or rowsum - colsum[col+1] in (grid[0][0], grid[-1][0]):
                        return True
                if cnt[colsum[col+1] - rowsum] > 0:
                    if col < cols-1 or colsum[col+1] - rowsum in (grid[0][cols-1], grid[-1][cols-1]):
                        return True
        return False
