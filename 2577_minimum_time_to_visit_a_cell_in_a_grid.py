class Solution:
    def minimumTime(self, grid: list[list[int]]) -> int:
        coords = {(0,0)}
        time = 0
        while coords:
            time += 1
            temp = set()
            while coords:
                row, col = coords.pop()
                if row == len(grid) - 1 and col == len(grid[0])-1:
                    return time -1
                for nrow in range(row-1, row+2, 2):
                    if nrow in range(0,len(grid)):
                        if grid[nrow][col] <= time:
                            temp.add((nrow, col))
                for ncol in range(col-1, col+2, 2):
                    if ncol in range(0, len(grid[0])):
                        if grid[row][ncol] <= time:
                            temp.add((row, ncol))
            coords = temp
        return -1

grid = [[0,1,3,2],
        [5,1,2,5],
        [4,3,8,6]]
output = 7

obj = Solution()
res = obj.minimumTime(grid)
print(output)
print(res)
print(res == output)