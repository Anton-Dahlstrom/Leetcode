class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row > 0 and col > 0:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
                elif row > 0:
                    grid[row][col] += grid[row-1][col]
                elif col > 0:
                    grid[row][col] += grid[row][col-1]
        return grid[len(grid)-1][len(grid[0])-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
output = 7

obj = Solution()
res = obj.minPathSum(grid)
print(res)
print(output)
print(res == output)
