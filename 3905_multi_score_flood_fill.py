class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        sources.sort(key=lambda x: x[2], reverse=True)
        grid = [[0]*m for _ in range(n)]

        def colorCell(row, col, color, grid):
            if row in range(0, len(grid)) and col in range(0, len(grid[0])) and grid[row][col] == 0:
                grid[row][col] = color
                return True
            return False

        for row, col, color in sources:
            grid[row][col] = color
        while sources:
            temp = []
            for row, col, color in sources:
                for drow, dcol in directions:
                    nrow, ncol = row+drow, col+dcol
                    if colorCell(nrow, ncol, color, grid):
                        temp.append([nrow, ncol, color])
            sources = temp
        return grid
