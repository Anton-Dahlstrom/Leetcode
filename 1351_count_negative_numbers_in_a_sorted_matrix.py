class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxcol = cols-1
        res = 0
        for row in range(rows):
            for col in range(maxcol, -2, -1):
                if col < 0:
                    return res
                if grid[row][col] >= 0:
                    break
                res += rows-row
            maxcol = col
            if maxcol < 0:
                break
        return res


grid = [[3, 2],
        [-3, -3],
        [-3, -3],
        [-3, -3]]
output = 6

obj = Solution()
res = obj.countNegatives(grid)
print(res)
print(output)
print(res == output)
