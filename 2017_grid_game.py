class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        if len(grid[0]) == 1:
            return 0

        for i in range(len(grid[0])-2,0,-1):
            grid[0][i] += grid[0][i+1]
        for i in range(1,len(grid[0])):
            grid[1][i] += grid[1][i-1]

        grid[0][0] = grid[0][1]

        best = min(grid[0][1], grid[1][-2])
        for i in range(1, len(grid[0])-1):
            best = min(best, max(grid[1][i-1], grid[0][i+1]))
        return best


grid = [[1,3,1,15],[1,3,3,1]]
output = 7


obj = Solution()
res = obj.gridGame(grid)
print(res)
print(output)
print(res == output)
        