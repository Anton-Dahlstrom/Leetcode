from typing import List


class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])
        vals = set()
        for row in range(rows):
            for col in range(cols):
                vals.add(grid[row][col])
                size = 1
                while row-size >= 0 and row+size < rows and col-size >= 0 and col+size < cols:
                    cur = grid[row-size][col] + grid[row+size][col] + \
                        grid[row][col-size] + grid[row][col+size]
                    botrow = row-size
                    toprow = row+size
                    for i in range(1, size):
                        cur += grid[botrow+i][col-i]
                        cur += grid[botrow+i][col+i]
                        cur += grid[toprow-i][col-i]
                        cur += grid[toprow-i][col+i]
                    vals.add(cur)
                    size += 1
        vals = list(vals)
        vals.sort(reverse=True)
        return vals[:3]
