class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        def isValid(row, col):
            if row in range(rows) and col in range(cols):
                return True
            return False

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        for srow in range(rows):
            for scol in range(cols):
                if (srow, scol) in visited or grid[srow][scol] == 0:
                    continue
                arr = [(srow, scol)]
                visited.add((srow, scol))
                val = 0
                while arr:
                    temp = []
                    for coord in arr:
                        row, col = coord
                        val += grid[row][col]
                        for drow, dcol in directions:
                            nrow = drow + row
                            ncol = dcol + col
                            if isValid(nrow, ncol) and (nrow, ncol) not in visited and grid[nrow][ncol]:
                                temp.append((nrow, ncol))
                                visited.add((nrow, ncol))
                    arr = temp
                if val % k == 0:
                    res += 1
        return res


grid = [[0, 2, 1, 0, 0], [0, 5, 0, 0, 5], [
    0, 0, 1, 0, 0], [0, 1, 4, 7, 0], [0, 2, 0, 0, 8]]
k = 5
output = 2

grid = [[0, 0, 0], [0, 0, 1], [11, 0, 6], [0, 10, 2], [0, 0, 0], [8, 0, 0]]
k = 19
output = 1


obj = Solution()
res = obj.countIslands(grid, k)
print(res)
print(output)
print(res == output)
