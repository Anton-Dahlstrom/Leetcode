class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        original = grid[row][col]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        changing = []

        def isValid(row, col):
            if row in range(rows) and col in range(cols):
                return True
            return False

        arr = [(row, col)]
        while arr:
            temp = []
            for row, col in arr:
                added = False
                for drow, dcol in directions:
                    nrow, ncol = row+drow, col+dcol
                    if (not isValid(nrow, ncol) or grid[nrow][ncol] != original) and not added:
                        added = True
                        changing.append((row, col))
                    if isValid(nrow, ncol) and (nrow, ncol) not in visited and grid[nrow][ncol] == original:
                        visited.add((nrow, ncol))
                        temp.append((nrow, ncol))
            arr = temp
        for row, col in changing:
            grid[row][col] = color
        return grid


grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
row = 1
col = 1
color = 2
output = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

obj = Solution()
res = obj.colorBorder(grid, row, col, color)
print(res)
print(output)
print(res == output)
